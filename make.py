#!/usr/bin/env python

import typer
import subprocess

make = typer.Typer()

def repository(image, tag):
    return f"qfortier/{image}:{tag}"

@make.command()
def build(image: str, tag: str="latest"):
    subprocess.run(["docker", "build", "-t", repository(image, tag), image])

@make.command()
def push(image: str, tag: str="latest"):
    build(image, tag)
    subprocess.run(["docker", "push", repository(image, tag)])

if __name__ == "__main__":
    make()
