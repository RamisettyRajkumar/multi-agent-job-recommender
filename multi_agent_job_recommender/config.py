# config.py - central config. Edit environment variables or this file to change keys.
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')  # set using export OPENAI_API_KEY="sk-..."
# If you prefer to hardcode (NOT recommended), you can set OPENAI_API_KEY = "your_key_here"
