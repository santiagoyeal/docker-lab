import os
import time
from db import Database


def run_exercises():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set")
        return

    db = Database(db_url)
    db.connect()

    print("Creating table 'items'...")
    db.create_table()

    print("Inserting sample data...")
    db.insert_item("apple", 5)
    db.insert_item("banana", 3)

    print("Current rows in 'items':")
    for row in db.select_all():
        print(row)

    print("Updating an item...")
    db.update_quantity("apple", 10)

    print("Deleting an item...")
    db.delete_item("banana")

    print("Final rows:")
    for row in db.select_all():
        print(row)

    db.disconnect()


if __name__ == "__main__":
    # wait for database to be ready
    print("Waiting for database...")
    time.sleep(5)
    run_exercises()
