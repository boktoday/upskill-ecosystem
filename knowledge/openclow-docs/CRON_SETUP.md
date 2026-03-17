# OpenClaw Docs Sync - Cron Setup

## Daily Sync

The knowledge base syncs daily to keep docs up-to-date.

## Setup Cron Job

```bash
# Add to crontab
crontab -e

# Add this line for daily sync at 2am:
0 2 * * * cd /path/to/upskill-ecosystem/knowledge/openclow-docs && python3 scraper.py >> sync.log 2>&1
```

## Manual Sync

```bash
cd knowledge/openclow-docs
python3 scraper.py
```

## Output

- Docs stored in: `knowledge/openclow-docs/content/`
- Index at: `knowledge/openclow-docs/content/index.json`
- Log at: `knowledge/openclow-docs/sync.log`
