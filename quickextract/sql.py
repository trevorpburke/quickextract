#!/usr/bin/env python

from sqlalchemy import create_engine
import pandas as pd

class SQL_Extract(object):
    def __init__(self, engine):
        self.engine = create_engine(engine)
    
    def csv(self, query, filename):
        df = pd.read_sql(query, self.engine)
        df.to_csv('{}.csv'.format(filename), index=False, encoding='utf-8')

    def xlsx(self, query, filename):
        df = pd.read_sql(query, self.engine)
        df.to_excel('{}.xlsx'.format(filename), index=False, encoding='utf-8',  sheet_name='Sheet1')
