from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/samsung/')
def samsung():
    return render_template('samsung.html')
    

@app.route('/kakao/')
def kakao():
    return render_template('kakao.html')

@app.route('/naver/')
def naver():
    return render_template('naver.html')

@app.route('/index/')
def index():
    return render_template('/ITindex/')


app.run

