import sqlite3

def run_sql_query(sql_query: str):
    try:
        conn = sqlite3.connect("sales.db")  # <-- ensure this points to your DB
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        return f"SQL Error: {e}"
