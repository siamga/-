from flask import Flask, render_template, request, redirect, url_for
from modules import mod_sql  #직접 만든 모듈(플라스크의 sql 접속 및 구문 작성 간소화)
import pandas as pd

app = Flask(__name__)
#__name__:지금 실행하는 파일 이름이 들어간다.

#localhost로 접속했을 때
@app.route("/")
def index():
    return render_template('index.html')

#localhost/signup으로 접속했을 때
@app.route("/signup/", methods=['GET'])
def signup():
    return render_template('signup.html')
#### 데이터를 get 형식으로 입력 받는 경우 -> request.args 형식으로 데이터를 호출
#### 데이터를 post 형식으로 입력 받는 경우 -> request.form 형식으로 데이터를 호출
#### url을 통해서 데이터를 전송하는 전송 방식 get 방식
#### url이 아닌 다른 어떤 방식을 통해서 url에 정보가 보이지 
#### 않는 방식으로 전송하는 전송 방식 post 방식

@app.route('/signup/', methods=["POST"])
def signup_2():

    signup = mod_sql.Databse()

    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]

    sql = """INSERT INTO user_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

    print(0)
    _values = [_id,_password,_name,_phone,_ads,_gender,_age,_regitdate]
    print(1)
    signup.execute(sql,_values)
    print(2)
    signup.commit()

    return redirect(url_for('index'))
    ## url_for(함수명): 해당 함수가 적힌 url 호출
    ## redirect(url): 적혀진 url로 돌아간다.(url이 지정되어있든 없든 해당 url로 이동한다. 결과값이 나올지는 모르겠지만...)

@app.route('/login/', methods=['POST'])
def login():
    login = mod_sql.Databse()
    _id = request.form["input_id"]
    _password = request.form["input_pw"]

    sql = '''SELECT * FROM user_info where ID = %s and password = %s'''
    values = [_id,_password]

    result = login.executeAll(sql,values)
    
    if result:
        return render_template('welcome.html', name = result[0]['name'], id =_id)
    
    else:
        return redirect(url_for('index'))

@app.route('/update/', methods=['GET'])
def update():
    id = request.args['_id']
    sql = 'SELECT * FROM user_info where ID = %s'
    values = [id]
    _db = mod_sql.Databse()
    result = _db.executeAll(sql,values)
    return render_template('update.html', info = result[0])

@app.route('/update/', methods=['POST'])
def update_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    sql = '''
          UPDATE user_info SET password = %s,
          name = %s, 
          phone = %s,
          gender = %s,
          age = %s,
          ads = %s
          WHERE ID = %s
         '''
    values = [_password,_name,_phone,_gender,_age,_ads,_id]
    _db = mod_sql.Databse()
    _db.execute(sql,values)
#cursor.execute(): 파이썬 상에서 sql 구문을 작동시키는 구문
#cursor.fetchall(): 피이썬 상에서 작동시킨 sql 구문의 결과값을 
    _db.commit()
#commit(): 파이썬에서 작업한 sql 구문 작업 내용을 실제 mysql 상에 적용시키는 명령어
    return redirect(url_for('index'))



# 회원탈퇴 
# welcome.html -> /delete url 접속: 로그인한 ID값으 같이 전송
#->delete 시에 password를 확인해야함 -> id,password가 db내에 존재하면 삭제
# 없으면 패스워드기 맞지 않습니다라는 메시지를 페이지에 띄운다.

@app.route('/delete/', methods=['GET'])
def delete():
    id = request.args['_id']
    return render_template('delete.html', _id = id)

@app.route('/delete/', methods=['POST'] )
def delete_2():

    id = request.form['_id']
    pw = request.form['_pw']

    sql_1 = 'SELECT * FROM user_info WHERE ID=%s and password = %s'
    sql_2 = 'DELETE FROM user_info WHERE ID=%s and password=%s'
    values = [id,pw]
    print(values)

    delete_2 = mod_sql.Databse()

    result = delete_2.executeAll(sql_1,values)

    print(4)

    if result:
        delete_2.execute(sql_2,values)
        delete_2.commit()
        return redirect(url_for('index'))

    else: #만일 존재하지 않음을 조건으로 건다면 if not으로 조건을 건다.
        return '패스워드가 맞지 않습니다.'


    #sql문을 사용해서 user_info left join ads_info -> 
    # columns호출: user_inofo:name,ads,age  ads_info: register_count
    # view.html을 render 쿼리문의 결과값을 데이터로 보내줘라.
@app.route('/view', methods=["GET"])
def _view():
    print(1)
    sql = '''SELECT user_info.name, user_info.ads, 
             user_info.age, ads_info.Register_count 
             FROM user_info LEFT JOIN ads_info 
             on user_info.ads = ads_info.ads'''
    
    print(2)
    db = mod_sql.Databse()
    print(4)
    result = db.executeAll(sql)
    print(result)
    key = list(result[0].keys())
    print(key)


    return render_template('view.html', result = result, key = key)

# html에서의 파이썬 코드 작성:{% 코드 %}
# 이 경우 코드의 종료를 위해서 {%end코드%}를 작성한다.
# html에서의 파이썬 변수 입력:{{ 변수 }}

app.run(port=8080)