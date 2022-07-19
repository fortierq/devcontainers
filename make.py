#!/usr/bin/env python

import json
from pathlib import Path
import subprocess
import typer

from settings import repository_to_devcontainer

make = typer.Typer()

def repository(image: str, tag: str) -> str:
    return f"qfortier/{image}:{tag}"

@make.command()
def build(image: str, tag: str="latest"):
    subprocess.run(["docker", "build", "-t", repository(image, tag), image])

@make.command()
def push(image: str, tag: str="latest"):
    build(image, tag)
    subprocess.run(["docker", "push", repository(image, tag)])

@make.command()
def devcontainer(name: str):
    d = dict()
    for p in Path(".").glob("**"):
        if p.is_dir() and p.name == name:
            for part in p.relative_to(".").parts:
                if (file := Path(part) / "devcontainer.json").exists():
                    d |= json.loads(file.read_text())
            
    
if __name__ == "__main__":
    make()
