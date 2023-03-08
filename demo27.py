import tushare as ts
import os

print(ts.__version__)

for code in open("stock_code.list"):
    code = code.strip()
    try:
        data = ts.get_hist_data(code)
        data.to_excel(code+'.xlsx')
    except:
        os.system("echo %s >> stock_none.list" % code)
        continue
exit()

