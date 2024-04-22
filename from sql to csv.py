from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Database connection settings
connection_string = 'DRIVER={SQL server};SERVER=SMEDINA-DELL;DATABASE=master;Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        phoneNumber = request.form['phoneNumber']

        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, phone_number) VALUES (?, ?, ?)", (firstName, lastName, phoneNumber))
        conn.commit()
        cursor.close()

        return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
