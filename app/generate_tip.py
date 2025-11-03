# app/generate_tip.py
import os
import json
from datetime import datetime
from pathlib import Path
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in the environment before running.")

openai.api_key = OPENAI_API_KEY

def generate_tip(prompt="Give me a concise AI engineering tip of the day (one short paragraph)."):
    # Use Chat Completions; adjust model to what you have access to
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # replace if you use another model
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides short AI engineering tips."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    # safe extraction
    text = resp["choices"][0]["message"]["content"].strip()
    return text

def save_tip(text: str, out_dir="artifacts"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    # Use more readable timestamp format: YYYY-MM-DD_HH-MM-SS
    ts = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = Path(out_dir) / f"tip_{ts}.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # also write a latest pointer
    latest = Path(out_dir) / "tip_of_day.txt"
    with open(latest, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return str(filepath)

if __name__ == "__main__":
    import sys
    
    tip = generate_tip()
    path = save_tip(tip)
    print(f"Saved tip to {path}")
    
    # Show turtle alert if --alert flag is provided
    if "--alert" in sys.argv:
        try:
            from .turtle_alert import show_tip_alert
            show_tip_alert(tip)
        except ImportError as e:
            print(f"Could not import turtle alert: {e}")
        except Exception as e:
            print(f"Error showing turtle alert: {e}")