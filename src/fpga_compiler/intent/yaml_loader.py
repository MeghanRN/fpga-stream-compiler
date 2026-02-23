
import yaml
from pathlib import Path

def load_pipeline_yaml(path: Path):
    return yaml.safe_load(path.read_text())
