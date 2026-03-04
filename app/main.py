import os
import time
from db import Database
from flask import Flask, jsonify

app = Flask(__name__)


def wait_for_db_and_connect(db_url, retries=10, delay=2):
    db = Database(db_url)
    for attempt in range(retries):
        try:
            db.connect()
            return db
        except Exception as e:
            print(f"Database not ready (attempt {attempt+1}/{retries}): {e}")
            time.sleep(delay)
    raise RuntimeError("Could not connect to the database")


def setup_db(db_url):
    db = wait_for_db_and_connect(db_url)
    print("Creating table 'items'...")
    db.create_table()
    print("Inserting sample data...")
    # Insert sample data if not present
    try:
        db.insert_item("apple", 5)
        db.insert_item("banana", 3)
    except Exception:
        pass
    return db


@app.route("/api/ping")
def ping():
    return "pong"


@app.route("/api/items")
def items():
    try:
        rows = app.db.select_all()
        return jsonify(rows)
    except Exception as e:
        return (str(e), 500)


def main():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set")
        return

    print("Setting up DB connection...")
    app.db = setup_db(db_url)

    # Start Flask dev server on 0.0.0.0:8000 so other services can reach it
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
