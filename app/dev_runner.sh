#!/bin/sh
# dev_runner.sh
# Usage: dev_runner.sh [script-to-run]
# Environment variables:
#   APP_SCRIPT - default script to run (default: main.py)
#   AUTO_RELOAD / DEV_MODE - if set to "true", run with watchmedo auto-restart

APP_SCRIPT="${1:-${APP_SCRIPT:-main.py}}"

if [ "${AUTO_RELOAD:-false}" = "true" ] || [ "${DEV_MODE:-false}" = "true" ]; then
  echo "[dev_runner] Starting with auto-reload -> ${APP_SCRIPT}"
  # Use the Python watcher (dev_runner.py) which uses watchgod (pure-Python)
  exec python /usr/src/app/dev_runner.py
else
  echo "[dev_runner] Starting without auto-reload -> ${APP_SCRIPT}"
  exec python "$APP_SCRIPT"
fi
