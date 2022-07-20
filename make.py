#!/usr/bin/env python

import json
import os
from pathlib import Path
import subprocess
import typer

from qfutils.ds import union_json

from settings import devcontainer_to_repository

make = typer.Typer()

def dockerhub(image: str, tag: str) -> str:
    return f"qfortier/{image}:{tag}"

@make.command()
def prune():
    subprocess.run(["docker", "system", "prune", "-a"])

@make.command()
def build(image: str, tag: str="latest"):
    dir = image
    if tag != "latest":
        dir = f"{image}/{tag}"
    subprocess.run(["docker", "build", "-t", dockerhub(image, tag), dir])

@make.command()
def push(image: str, tag: str="latest"):
    build(image, tag)
    subprocess.run(["docker", "push", dockerhub(image, tag)])

@make.command()
def run(image: str, tag: str="latest"):
    shell = "/bin/bash"
    if tag == "alpine":
        shell = "/bin/ash"
    subprocess.run(["docker", "run", "-it", "--rm", dockerhub(image, tag), shell])

def devcontainer(name: str):
    with open(f"{name}/devcontainer.json") as f:
        d = json.load(f)
        if "inherits" in d:
            for p in d["inherits"]:
                d = union_json(d, devcontainer(p))
            del d["inherits"]
        return d

@make.command()
def update(dev: str="all"):
    if dev == "all":
        for dev in devcontainer_to_repository:
            update(dev)
    else:
        d = devcontainer(dev)
        tmp = "/tmp/repo"
        for repo in devcontainer_to_repository[dev]:
            os.chdir("/tmp")
            subprocess.run(["rm", "-rf", "repo"])
            subprocess.run(["git", "clone", f"https://www.github.com/{repo}", "repo"])
            os.chdir(tmp)
            file = f".devcontainer/devcontainer.json"
            Path(file).parent.mkdir(parents=True, exist_ok=True)
            Path(file).write_text(json.dumps(d, indent=4))
            subprocess.run(["git", "add", str(file)])
            subprocess.run(["git", "commit", "-m", "Update devcontainer.json", "-q"])
            subprocess.run(["git", "push"])
    
if __name__ == "__main__":
    make()
