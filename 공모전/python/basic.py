import pandas as pd
import numpy as np

class read():
    cd = pd.read_csv('..\자료\기업신용등급비율.csv',encoding='cp949')
    #전체 연도 대상 기업 신용등급 분포 비율

    def __init__(self,url):
        self.url = url

    def tidy(self):
        self.loan = pd.read_csv(self.url, encoding='cp949')
        self.loan.columns =  ['은행','구분','1~3등급','4등급','5등급','6등급','7~10등급','평균금리','참고사항']
        self.loan.drop(0,axis=0,inplace=True)
        self.loan.drop(['구분','참고사항','평균금리'],axis=1,inplace=True)
        self.loan.replace('-',0,inplace=True)
        self.loan.reset_index(drop=True, inplace=True)
        return self.loan   #url 지정 해당 연도의 특정 대출의 은행별 금리 처리

    def multi(self,year):
        self.a = []
        # a = 추후 은행별 가중평균 수익률 정리예정
        self.partial_cd = np.array(self.cd[year],dtype='float')
        # 지정하고 싶은 연도의 신용등급 분포 비율
        for i in range(len(self.loan)):

            self.interest = np.array(self.loan.loc[i:i,'1~3등급':'7~10등급'],dtype='float')[0]
            #특정 은행의 등급별 대출 금리
            
            self.boolean = self.interest.astype('bool')
            #해당 은행의 대출 타겟 판별

            self.real_tot = sum(self.partial_cd * self.boolean)
            #전체 신용등급 고객 대비 타겟 대상 비율
            
            self.real_customer_ration = (self.partial_cd/self.real_tot)
            #타겟 고객 대비 특정 등급 고객 비율

            self.real_interest = self.real_customer_ration @ self.interest
            #타겟 고객 대비 특정 등급 고객 비율로 구한 은행의 가중 평균 금리

            self.a.append(self.real_interest)

        return self.a

def bank_db(bank,mort,credit,minusave):
    bank_list = list(bank)
    bank_df = pd.DataFrame(bank_list,columns=['bank'])
    bank_df['mort']=mort
    bank_df['credit']=credit
    bank_df['minusave']=minusave

    return bank_df


    # list = db.loc[:,'mort':'minusave'].sum()/16
    # return list.sum()/3





