#!/usr/bin/env python3
"""
OpenClaw Documentation Scraper
Downloads and stores docs.openclaw.ai locally for knowledge base
"""

import os
import json
import hashlib
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

DOCS_URL = "https://docs.openclaw.ai/"
OUTPUT_DIR = Path(__file__).parent / "content"

# Common doc file extensions
DOC_EXTENSIONS = {'.md', '.html', ''}

def get_local_path(url, base_url=DOCS_URL):
    """Convert URL to local file path"""
    parsed = urlparse(url)
    path = parsed.path.lstrip('/')
    
    if not path or path.endswith('/'):
        path += 'index'
    
    if not any(path.endswith(ext) for ext in DOC_EXTENSIONS):
        path += '.md'
    
    return OUTPUT_DIR / path

def fetch_page(url):
    """Fetch a single page"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_links(html_content, base_url=DOCS_URL):
    """Extract markdown links from HTML or find .md links"""
    import re
    # Find markdown-style links [text](./path.md)
    links = re.findall(r'href=["\']([^"\']+\.md)["\']', html_content)
    # Also find relative links
    links += re.findall(r'href=["\']([^"\']+)["\']', html_content)
    return [urljoin(base_url, link) for link in links if not link.startswith(('http', '#', 'mailto'))]

def compute_hash(content):
    """Compute content hash"""
    return hashlib.md5(content.encode()).hexdigest()

def load_index():
    """Load the document index"""
    index_file = OUTPUT_DIR / "index.json"
    if index_file.exists():
        with open(index_file) as f:
            return json.load(f)
    return {"pages": {}, "last_sync": None}

def save_index(index):
    """Save the document index"""
    index_file = OUTPUT_DIR / "index.json"
    with open(index_file, 'w') as f:
        json.dump(index, f, indent=2)

def sync_docs():
    """Main sync function"""
    print(f"🔄 Starting OpenClaw docs sync at {datetime.now()}")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    index = load_index()
    to_fetch = [DOCS_URL]
    fetched = set()
    
    # Simple fetch - just get main page for now
    url = DOCS_URL
    content = fetch_page(url)
    
    if content:
        local_path = get_local_path(url)
        local_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert HTML to markdown if needed
        if url.endswith('.md'):
            with open(local_path, 'w') as f:
                f.write(content)
        else:
            # Save as markdown
            md_content = f"# OpenClaw Documentation\n\nSource: {url}\n\n{content}"
            with open(local_path.with_suffix('.md'), 'w') as f:
                f.write(md_content)
        
        # Update index
        content_hash = compute_hash(content)
        index["pages"][url] = {
            "local_file": str(local_path),
            "hash": content_hash,
            "fetched": datetime.now().isoformat()
        }
        print(f"✅ Downloaded: {url}")
    
    # Update last sync time
    index["last_sync"] = datetime.now().isoformat()
    save_index(index)
    
    print(f"✅ Sync complete! {len(index['pages'])} pages")

if __name__ == "__main__":
    sync_docs()
