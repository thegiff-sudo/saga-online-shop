import sys
import os
from pathlib import Path

# Add project root to sys.path so app modules import cleanly on Vercel
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from app.main import app

# Export app for Vercel Serverless Function handler
# Vercel's Python runtime natively detects ASGI 'app'
