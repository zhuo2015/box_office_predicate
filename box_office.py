# coding:uft-8

import pandas as pd
import requests

json11 = "http://www.cbooo.cn/BoxOffice/GetHourBoxOffice?d=1485874026355"
url_xml = 'http://www.cbooo.cn/BoxOffice/GetHourBoxOffice'
tt = requests.get(url_xml)

ss = tt.json()
ddf = pd.DataFrame(ss['data2'])
ddf.columns =['实时票房','排名', 'xxx','片名','票房占比','xxx','上映天数', '累计票房']
del ddf['xxx']
ddf.reindex(columns=['排名', '片名','实时票房','票房占比','上映天数', '累计票房','xxxid'])
