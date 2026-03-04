import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self, url):
        self.url = url
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(self.url)
        self.conn.autocommit = True

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    quantity INTEGER NOT NULL
                );
                """
            )

    def insert_item(self, name, quantity):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO items (name, quantity) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;",
                (name, quantity),
            )

    def select_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchall()

    def update_quantity(self, name, quantity):
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE items SET quantity = %s WHERE name = %s;",
                (quantity, name),
            )

    def delete_item(self, name):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM items WHERE name = %s;", (name,))
