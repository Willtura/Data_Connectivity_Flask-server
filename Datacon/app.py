from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def display_temperature():
    # Verbind met de SQLite-database
    conn = sqlite3.connect('MKR_database.db')
    cursor = conn.cursor()

    # Voer een query uit om temperatuurgegevens op te halen met de meest recente tijdstempel
    cursor.execute('SELECT * FROM "sensor_data" WHERE timestamp = (SELECT MAX(timestamp) FROM sensor_data);')
    datalatest = cursor.fetchall()

    # Sluit de databaseverbinding
    conn.close()

    return render_template('temperatuur.html',datalatest=datalatest)

@app.route('/historical')
def display_historical_data():
    # Verbind met de SQLite-database
    conn = sqlite3.connect('MKR_database.db')
    cursor = conn.cursor()

    # Voer een query uit om historische temperatuurgegevens op te halen (voorbeeld: laatste 10 records)
    cursor.execute('SELECT * FROM "sensor_data" ORDER BY timestamp DESC LIMIT 100;')
    historical_data = cursor.fetchall()

    # Sluit de databaseverbinding
    conn.close()

    return render_template('historical.html', historical_data=historical_data)






if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host='0.0.0.0',port=5000)


