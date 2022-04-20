from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second/')
def second(): 
    _id = request.args.get("id")
    _pass =request.args.get('pass')
    print(_id,_pass)

    return render_template('second.html', id = _id)
    #if _id == 'asd' and _pass == 'qwe':
    #    return render_template('second.html')
    #else:
    #    return '로그인에 실패했습니다.'
#render_template()과정을 통해서 
#/second/페이지에 second.html파일을 웹에 띄움

@app.route('/third/', methods=['POST'])
def third():
    _id = request.form['id']
    _pass = request.form['pass']
    print(_id,_pass)
    if _id == 'asd' and _pass == 'qwe':
        return 'asd님께서 post 방식 로그인에 성공하셨습니다.'
    else:
        return render_template('fail.html')
#그냥 /third/페이지에 문자 출력

@app.route('/colxrow/')
def colxrow():
    return render_template('colxrow.html')

app.run

