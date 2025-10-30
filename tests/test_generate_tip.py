# tests/test_generate_tip.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app.generate_tip import save_tip

def test_save_tip(tmp_path):
    sample = "Test tip: use small experiments to validate prompts."
    out_file = save_tip(sample, out_dir=tmp_path)
    p = Path(out_file)
    assert p.exists()
    content = p.read_text()
    assert "Test tip" in content
