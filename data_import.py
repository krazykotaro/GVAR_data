#-*- coding: utf-8 -*-

import pandas as pd
import requests
import psycopg2

#USのGDPを取得
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/Q.US.NGDP_R_CH_SA_XDC?startPeriod=1957&endPeriod=2016'

# Get data from the above URL using the requests package
data = requests.get(url).json()

# Load data into a pandas dataframe
base_year = pd.DataFrame(data['CompactData']['DataSet']['Series'])["@BASE_YEAR"]
country = pd.DataFrame(data['CompactData']['DataSet']['Series'])["@REF_AREA"]
obs = pd.DataFrame(data['CompactData']['DataSet']['Series']['Obs'])
# データを連結
data = pd.concat([base_year, country, obs], axis = 1)

#データを整理
data.columns = ["base_year", "country", "rgdp", "time"]
data = data.ix[:, ["time", "country", "rgdp", "base_year"]]

#データベースに接続
connection = psycopg2.connect("host=rds-for-data.csjbwxuxnbph.ap-northeast-1.rds.amazonaws.com por dbname=sampledb user=sayamada password=pssword")
