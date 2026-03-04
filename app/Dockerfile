FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# make sure our dev runner can be executed (safe even if file is bind-mounted)
RUN chmod +x /usr/src/app/dev_runner.sh || true

# Entrypoint runs the dev runner script which will either start normally
# or, when AUTO_RELOAD/DEV_MODE is set, use watchmedo to reload on changes.
ENTRYPOINT ["sh", "/usr/src/app/dev_runner.sh"]
CMD ["main.py"]
