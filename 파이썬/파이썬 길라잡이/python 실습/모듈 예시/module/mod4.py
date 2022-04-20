import pandas as pd
import numpy as np

class sales():
    def __init__(self,url):
        self.url = url

    def tidy(self,input_sort='Country',input_inplace=True):
        self.df = pd.read_csv(self.url)
        self.df.sort_values(input_sort,inplace=input_inplace)
        self.df.reset_index(drop=True, inplace=input_inplace)
        return self.df
    
    def columns(self,_list = []):
        self.df.drop(_list,axis=1,inplace=True)
        return self.df
    
    def re_name(self,col):
        self.df.columns = col
        return self.df

    def grouping(self,col,nation):
        self.total = self.df.groupby(col).get_group(nation)
        return self.total

    def drop_set(self,start,end):
        self.df.drop(self.df.loc[:,start:end],axis=1,inplace=True)
        return self.df
    