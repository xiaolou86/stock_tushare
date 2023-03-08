import tushare as ts
import os
#ts.get_hist_data('600848')

print(ts.__version__)

ts.set_token('921869c2b013385aee2bc233e98063f77b812cfc43c943a6babcb987')

pro = ts.pro_api()
#df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#print(df)

#data=ts.get_hist_data('300274',start='2017-01-01',end='2018-03-27')
#print(data)

#df = pro.daily_basic(ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
#df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#print(df)
#df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')


rows=5108

offset = 0
limit = 50
while offset<=rows:
    data = pro.stock_basic(exchange='', limit=limit, offset=offset, list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    offset += limit
    os.system('echo "%s" >> stock.list' % data)

#data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')



