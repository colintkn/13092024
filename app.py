from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",  # Change to your DB name
        user="db-user01",
        password=os.getenv('DB_PASSWORD')  # Use environment variable for security
    )
    return conn


@app.route('/hello')
def hello_world():
    return jsonify(message="hello world!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5656)

# New endpoint to fetch data from the database
@app.route('/employees')
def get_data():
    try:
        # Connect to the database
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Execute a query (assuming there is a 'sample_table' with 'data' column)
        cur.execute('SELECT id, name, title, department, hire_date FROM employees;')
        rows = cur.fetchall()
        
        # Close the connection
        cur.close()
        conn.close()

        employees = []
        for row in rows:
            employees.append({
                'id': row[0],
                'name': row[1],
                'title': row[2],
                'department': row[3],
                'hire_date': row[4],
            })

        if employees:
            return jsonify(employees=employees)
        else:
            return jsonify(message="No employees found")
    except Exception as e:
        return jsonify(error=str(e)), 500
