from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Database connection settings
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

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
    app.run(debug=True)
