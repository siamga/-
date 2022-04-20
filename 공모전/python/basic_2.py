import basic
import numpy as np
import pandas as pd

def db(year):
    bank = pd.read_csv('..\자료\은행대출_금리\_%d\물적담보대출.csv'%(year), encoding='cp949')

    bank.columns =  ['은행','구분','1~3등급','4등급','5등급','6등급','7~10등급','평균금리','참고사항']
    bank.drop(0,axis=0,inplace=True)
    bank.drop(['구분','참고사항','평균금리'],axis=1,inplace=True)
    bank.replace('-',0,inplace=True)
    bank.reset_index(drop=True, inplace=True)
    bank = bank['은행']
    bank

    credit_year = basic.read('..\자료\은행대출_금리\_%d\신용대출.csv'%(year))
    credit_year.tidy()
    credit = credit_year.multi('%d년말'%(year-1))

    
    mort_year = basic.read('..\자료\은행대출_금리\_%d\물적담보대출.csv'%(year))
    mort_year.tidy()
    mort = mort_year.multi('%d년말'%(year-1))
    mort

    minusave_year = basic.read('..\자료\은행대출_금리\_%d\신용마통대출.csv'%(year))
    minusave_year.tidy()
    minusave = minusave_year.multi('%d년말'%(year-1))

    db = basic.bank_db(bank,mort,credit,minusave)
    list = db.loc[:,'mort':'minusave'].sum()/16
    result = list.sum()/3
    return result