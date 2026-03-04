#!/usr/bin/env python3
"""Simple file-watcher runner using watchgod.

It launches the target Python script and restarts it when any file in the
project tree changes (useful when the project dir is mounted as a volume).
"""
import os
import subprocess
import sys
from watchgod import watch

SCRIPT = os.environ.get("APP_SCRIPT", "main.py")
WATCH_PATH = os.environ.get("WATCH_PATH", ".")

def run_script():
    print(f"[dev_runner.py] Starting: {SCRIPT}")
    return subprocess.Popen([sys.executable, SCRIPT])

if __name__ == "__main__":
    proc = run_script()
    try:
        for changes in watch(WATCH_PATH):
            print("[dev_runner.py] Detected changes:", changes)
            proc.kill()
            proc.wait()
            proc = run_script()
    except KeyboardInterrupt:
        print("[dev_runner.py] Stopping (KeyboardInterrupt)")
        proc.kill()
        proc.wait()
