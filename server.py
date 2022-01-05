#!/usr/bin/env python3
from typing import Optional
import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/{command}")
def read_root(command: str):
    command.replace("%20", " ")
    stream = os.popen(f'renault-api {command}')
    output = stream.read()
    return output

