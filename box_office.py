# coding:uft-8

import pandas as pd
import requests

url_box = 'http://www.cbooo.cn/'
box_re = requests.get(url_box).content
box_df = pd.read_html(box_re)[0]
del box_df['Unnamed: 7']
del box_df['Unnamed: 0']