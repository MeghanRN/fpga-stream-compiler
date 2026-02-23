
from pathlib import Path
import argparse
from rich.console import Console
from fpga_compiler.intent.yaml_loader import load_pipeline_yaml

console = Console()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pipeline", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    ir = load_pipeline_yaml(Path(args.pipeline))
    console.print("[green]Parsed IR successfully[/green]")
