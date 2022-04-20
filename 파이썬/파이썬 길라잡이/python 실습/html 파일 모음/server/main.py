from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world'

#url을 추가해서 def를 실행하려면 어떻게 해야하는가?

@app.route('/zzz/')
#왜 '/'부호를 넣는가?
#해당 부호를 넣지 않는다면 
#url이 다음과 같다.
#http://127.0.0.1:5000zzz
#이때, 원래 해당 프로그램이 돌고 있는 장소는
# 5000인데  이게 구분자 없이 5000zzz로 바뀌어 
#존재하지 않는 주소로 들어가게 되어 실행되지 않는 것이다.
#따라서 /를 넣고 나중에 주소를 칠 때, 맨 마지막에 /를 
#넣는 경우 코드에 넣지 않으면 오류가 날 수 있기에 
#코드에도 /를 넣어 주는 것이 좋다.

def z():
    return '졸리구나~~~'

@app.route('/zzz/wow/')
def wow():
    return 'WOW!!!!!!!!!!!!'

app.run