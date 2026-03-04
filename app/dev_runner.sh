#!/bin/sh
# dev_runner.sh
# Usage: dev_runner.sh [script-to-run]
# Environment variables:
#   APP_SCRIPT - default script to run (default: main.py)
#   AUTO_RELOAD / DEV_MODE - if set to "true", run with watchmedo auto-restart

APP_SCRIPT="${1:-${APP_SCRIPT:-main.py}}"

if [ "${AUTO_RELOAD:-false}" = "true" ] || [ "${DEV_MODE:-false}" = "true" ]; then
  echo "[dev_runner] Starting with auto-reload -> ${APP_SCRIPT}"
  # watchmedo comes from the watchdog package (installed via requirements.txt)
  # pattern matches Python files; recursive so changes in submodules restart too
  exec watchmedo auto-restart --recursive --pattern="*.py" -- python "$APP_SCRIPT"
else
  echo "[dev_runner] Starting without auto-reload -> ${APP_SCRIPT}"
  exec python "$APP_SCRIPT"
fi
