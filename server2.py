from flask import Flask, request
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = db_connect.connect() # connect to database
    query = conn.execute("select * from employees") # This line performs query and returns json result
    return jsonify({'employees': [i[0] for i in query.cursor.fetchall()]}) # Fetches first column that is Employee ID

if __name__ == '__main__':
     app.run(port='5003')
     