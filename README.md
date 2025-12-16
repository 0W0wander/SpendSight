# Spendsight

Personal budget tracker that syncs with Google Sheets.

## Features

- Upload Chase and Discover CSV exports
- Auto-detect bank format
- Categorize with auto-tagging rules
- Track needs vs wants (50/30/20)
- Sync to Google Sheets
- Visual spending dashboard
- Sweep rules to filter transactions
- Windows system tray mode

## Setup

```bash
pip install -r requirements.txt
python run.py
```

Follow the setup wizard to connect Google Sheets.

## Build

```bash
pyinstaller run.spec
```
