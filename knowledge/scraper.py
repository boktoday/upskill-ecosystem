#!/usr/bin/env python3
"""
OpenClaw Documentation Scraper

Scrapes the local OpenClaw documentation to keep the knowledge base current.
Processes markdown files and extracts key concepts for the learning system.
"""

import os
import json
import hashlib
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Configuration
OPENCLAW_DOCS_PATH = r"C:\Users\Brendan\OneDrive\Downloads\ClawLauncher-Windows\myclaw\node_modules\openclaw\docs"
KNOWLEDGE_BASE_PATH = Path(__file__).parent
OUTPUT_FILE = KNOWLEDGE_BASE_PATH / "openclaw_docs.json"
STATE_FILE = KNOWLEDGE_BASE_PATH / ".scraper_state.json"

class OpenClawDocScraper:
    """Scraper for OpenClaw documentation."""
    
    def __init__(self):
        self.docs_path = Path(OPENCLAW_DOCS_PATH)
        self.state = self._load_state()
        self.knowledge_base = []
        
    def _load_state(self) -> Dict:
        """Load previous scrape state for change detection."""
        if STATE_FILE.exists():
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        return {"last_run": None, "file_hashes": {}}
    
    def _save_state(self):
        """Save current scrape state."""
        self.state["last_run"] = datetime.now().isoformat()
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def _compute_hash(self, content: str) -> str:
        """Compute hash for change detection."""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def _extract_title(self, content: str, filepath: Path) -> str:
        """Extract title from markdown content."""
        # Try to find H1
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        # Fallback to filename
        return filepath.stem.replace('-', ' ').title()
    
    def _extract_sections(self, content: str) -> List[Dict]:
        """Extract sections from markdown content."""
        sections = []
        current_section = None
        current_content = []
        
        for line in content.split('\n'):
            # Check for headers
            header_match = re.match(r'^(#{1,3})\s+(.+)$', line)
            if header_match:
                # Save previous section
                if current_section:
                    sections.append({
                        "level": current_section["level"],
                        "title": current_section["title"],
                        "content": '\n'.join(current_content).strip()
                    })
                # Start new section
                level = len(header_match.group(1))
                title = header_match.group(2).strip()
                current_section = {"level": level, "title": title}
                current_content = []
            else:
                if current_section:
                    current_content.append(line)
        
        # Save last section
        if current_section and current_content:
            sections.append({
                "level": current_section["level"],
                "title": current_section["title"],
                "content": '\n'.join(current_content).strip()
            })
        
        return sections
    
    def _extract_code_examples(self, content: str) -> List[Dict]:
        """Extract code examples from markdown."""
        examples = []
        code_blocks = re.findall(r'```(\w+)?\n(.*?)```', content, re.DOTALL)
        for lang, code in code_blocks:
            examples.append({
                "language": lang or "text",
                "code": code.strip()
            })
        return examples
    
    def _process_file(self, filepath: Path) -> Optional[Dict]:
        """Process a single markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for changes
            file_hash = self._compute_hash(content)
            relative_path = str(filepath.relative_to(self.docs_path))
            
            if relative_path in self.state["file_hashes"]:
                if self.state["file_hashes"][relative_path] == file_hash:
                    return None  # No changes
            
            self.state["file_hashes"][relative_path] = file_hash
            
            # Extract information
            doc = {
                "source": "openclaw-docs",
                "filepath": relative_path,
                "title": self._extract_title(content, filepath),
                "last_modified": datetime.fromtimestamp(filepath.stat().st_mtime).isoformat(),
                "hash": file_hash,
                "sections": self._extract_sections(content),
                "code_examples": self._extract_code_examples(content),
                "raw_content": content[:10000]  # First 10KB for search
            }
            
            return doc
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            return None
    
    def scrape(self) -> Dict:
        """Run the scraper on OpenClaw docs."""
        print(f"Scanning OpenClaw docs at: {self.docs_path}")
        
        if not self.docs_path.exists():
            return {
                "status": "error",
                "message": f"Docs path not found: {self.docs_path}",
                "files_processed": 0,
                "files_changed": 0
            }
        
        files_processed = 0
        files_changed = 0
        
        # Find all markdown files
        markdown_files = list(self.docs_path.rglob("*.md"))
        print(f"Found {len(markdown_files)} markdown files")
        
        for filepath in markdown_files:
            files_processed += 1
            doc = self._process_file(filepath)
            if doc:
                self.knowledge_base.append(doc)
                files_changed += 1
                print(f"  ✓ Updated: {doc['filepath']}")
        
        # Save results
        result = {
            "scraped_at": datetime.now().isoformat(),
            "source": "openclaw-docs",
            "files_processed": files_processed,
            "files_changed": files_changed,
            "documents": self.knowledge_base
        }
        
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(result, f, indent=2)
        
        self._save_state()
        
        return {
            "status": "success",
            "files_processed": files_processed,
            "files_changed": files_changed,
            "output": str(OUTPUT_FILE)
        }
    
    def get_status(self) -> Dict:
        """Get current scraper status."""
        return {
            "last_run": self.state.get("last_run"),
            "tracked_files": len(self.state.get("file_hashes", {})),
            "docs_path": str(self.docs_path),
            "docs_exist": self.docs_path.exists()
        }

def main():
    """CLI entry point."""
    import sys
    
    scraper = OpenClawDocScraper()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        status = scraper.get_status()
        print(json.dumps(status, indent=2))
    else:
        result = scraper.scrape()
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
