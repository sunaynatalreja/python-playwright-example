import yaml
from pathlib import Path

def load_settings():
    yaml_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)
