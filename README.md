# Docker Lab with Python and PostgreSQL

This project provides a simple lab environment using Docker, Python, and PostgreSQL. It can be used to run exercises or experiments connecting to a Postgres database from a Python application.

## Structure

- `docker-compose.yml`: Defines two services:
  - `db`: PostgreSQL database container.
  - `app`: Python application container that runs a script performing database operations.
- `app/`: Contains the Python application and Dockerfile.
  - `main.py`: Entrypoint script demonstrating basic CRUD operations.
  - `db.py`: Helper module for database interactions.
  - `requirements.txt`: Python dependencies.

## Getting started

1. **Build and start containers**

   ```sh
   cd /Users/santiago/Documents/Dev/dev-labs/docker-lab
   docker-compose up --build
   ```

2. **Observe output**

   The Python app will wait a few seconds for the database to start, then create a table, insert sample data, perform queries, updates, and deletions. The output will be printed to the console.

3. **Run custom exercises**

   You can modify `app/main.py` to implement your own exercises. The database URL is provided via the `DATABASE_URL` environment variable.

4. **Connect from host (optional)**

   You can use any Postgres client and connect to `localhost:5432` with credentials:
   - user: `labuser`
   - password: `labpassword`
   - database: `labdb`

5. **Stop and clean up**

   ```sh
   docker-compose down -v
   ```

Feel free to extend the project with additional tables, web APIs, or GUI components.
