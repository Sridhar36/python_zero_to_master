import psycopg2

def fetch_users():
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="myuser",
        password="mypassword",
        port=5432
    )

    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM users WHERE is_active = true;")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    fetch_users()
