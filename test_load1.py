# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:27:35 2017

@author: khabi
"""

import pandas as pd
from glob import glob 

import matplotlib.pyplot as plt

class Tsv_timeseries:
    """
    класс для загрузки данных нескольких файло в один
    """    
    def __init__(self,file_path):
        self._path = file_path
        self.df = pd.DataFrame()
        self.file_name_mask = '*.tsv'
        self.files = glob(self._path+self.file_name_mask) 
        print(len(self.files) , ' файлов найдено')
        #self.count_files = 0   # number of cases loaded
        self.parser = lambda date: pd.to_datetime(date, unit='ms')
        
    def load_tsv(self, name):
        self.df=pd.read_csv(name, 
                            delim_whitespace= True, 
                            index_col=0,
                            parse_dates=True, 
                            date_parser=self.parser)
        print('read ' + name + 'done')
        
    def load_tsvs(self):
        df = []
        for fl in self.files:    # iterating through all files
            df1=pd.read_csv(fl, 
                            delim_whitespace= True, 
                            index_col=0,
                            parse_dates=True, 
                            date_parser=self.parser)
            print('read ' + fl + 'done')
            df.append(df1)
        self.df = pd.concat(df)
        
#tdf = Tsv_timeseries('')
#tdf.load_tsv('1.tsv')

