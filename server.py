import pandas as pd
from flask import Flask, request, send_file, render_template
import flask
from io import StringIO
from models.model import getExcel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('download.html')

@app.route('/api/makeexcel', methods=['POST'])
def result():
    value = request.form['channelId']
    model = getExcel(value)
    fileName = model.get_excel()
    
    if fileName == 'null':
        my_res = flask.Response('잘못된 채널 id를 입력했습니다!')
        my_res.headers["Access-Control-Allow-Origin"] = "*"
        return my_res
    return send_file(fileName, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)
    #app.run(debug=True, port="8000")