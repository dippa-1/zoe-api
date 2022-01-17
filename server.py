#!/usr/bin/env python3
from typing import Optional
import os
from fastapi import FastAPI, BackgroundTasks
from time import sleep

app = FastAPI()

def execute_delayed(command: str, delay: int):
    if delay > 0:
        sleep(delay)
        stream = os.popen(command)
        output = stream.read()
        print(output)


@app.get("/{command}")
def read_root(command: str, background_tasks: BackgroundTasks, delay: Optional[str] = None):
    command.replace("%20", " ")
    cmd = f'renault-api {command}'
    if delay != None:
        delay = int(delay) * 60
        background_tasks.add_task(execute_delayed, cmd, delay)
        return cmd, str(delay) + 's'
    else:
        stream = os.popen(cmd)
        output = stream.read()
        return output
