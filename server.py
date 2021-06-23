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

@app.route('/api/getresult', methods=['POST'])
def download():
    value = request.form['channelId']
    result_pd = getExcel((str(value)))
    print(type(result_pd))
    print('ok')
    
    my_res = flask.Response('success!')
    my_res.headers["Access-Control-Allow-Origin"] = "*"
    
    return my_res

if __name__ == "__main__":
    app.run(port="8000", debug=True)
    #app.run(debug=True, port="8000")