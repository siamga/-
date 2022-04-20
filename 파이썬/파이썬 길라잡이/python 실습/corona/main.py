from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/corona/')
def corona():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns = ['인덱스','등록일시','누적사망자','누적확진자','게시글번호','기준일','기준시간','수정일시','누적의심자','누적확진률']
    corona_df.drop(columns=['기준일','기준시간','수정일시','게시글번호'],axis=1,inplace=True)
    corona_df.sort_values(['등록일시'],inplace=True)
    corona_df.reset_index(drop=True,inplace=True)
    corona_df['일일사망자'] = (corona_df['누적사망자']-corona_df['누적사망자'].shift()).fillna(0)
    corona_df['일일확진자'] = (corona_df['누적확진자'].diff()).fillna(0)
    corona_dict = corona_df.head(10).to_dict()
    cnt = len(corona_dict['등록일시'].keys())

    return render_template('corona.html', result = corona_dict,cnt =cnt)
    #return corona_df.to_html()

    
@app.route('/img2/')

def img2():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns = ['인덱스','등록일시','누적사망자','누적확진자','게시글번호','기준일','기준시간','수정일시','누적의심자','누적확진률']
    corona_df.drop(columns=['기준일','기준시간','수정일시','게시글번호'],axis=1,inplace=True)
    corona_df.sort_values(['등록일시'],inplace=True)
    corona_df.reset_index(drop=True,inplace=True)
    corona_df['일일사망자'] = (corona_df['누적사망자']-corona_df['누적사망자'].shift()).fillna(0)
    corona_df['일일확진자'] = (corona_df['누적확진자'].diff()).fillna(0)

    a = corona_df.head(10)['일일확진자'].values.tolist()
    time = corona_df.head(10)['등록일시'].values.tolist()
    plt.bar(time,a)

    img_2 = BytesIO()
    plt.savefig(img_2, format = 'png', dpi = 200)
    img_2.seek(0)

    return send_file(img_2, mimetype = 'image/png')


@app.route('/img/')
def img():
    values = [1,2,3]
    plt.plot(values)

    img_1 = BytesIO()
    plt.savefig(img_1,format='png',dpi = 200)
    img_1.seek(0)

    return send_file(img_1,mimetype='image/png')

app.run