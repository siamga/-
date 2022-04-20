from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first/')
def first():
    return render_template('first.html')

@app.route('/second/')
def second():
    _id = request.args.get('id')
    _pass = request.args.get('pass')
    print(_id,_pass)

    if _id == 'asd' and _pass == 'qwe':
        return render_template('second.html',id=_id)
    else:
        return render_template('third.html')

@app.route('/third/',methods=['POST'])
def third():
    _id = request.form['id']
    _pass = request.form['pass']
    print(_id,_pass)

    if _id == 'asd' and _pass == 'qwe':
        return render_template('fourth.html',id=_id)
    else:
        return render_template('third.html')

@app.route('/fifth/')
def fifth():
    return '잘못된 로그인 정보입니다.'