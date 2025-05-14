from flask import Flask, render_template, request, redirect, url_for
from cosmos_client import CosmosDBClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cosmos_client = CosmosDBClient()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    read_result = None

    if request.method == 'POST':
        if 'write' in request.form:
            value = request.form['value']
            cosmos_client.write_item(value)
            message = "Data written successfully."

        elif 'read' in request.form:
            consistency = request.form['consistency']
            read_result = cosmos_client.read_latest_item(consistency)

    return render_template('index.html', message=message, result=read_result)

if __name__ == '__main__':
    app.run(debug=True)
