# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZUpjEizy0bZXwMvoPW7p3rvrQVqwBZjX
"""

import re
def convert(s):
  an=","
  return s.group()+","

f = open("data.txt", "r")
s2=f.read()
s1='curl -X POST -H "Content-type:application/json" -d  "{\"instances\":['
s3= ']]]]}" http:/localhost:9002/v1/models/mnist_experiments:predict'
s2=s2.replace("\n", "")
s2=re.sub(r"[0-9]\s+",convert,s2)
# s2=s2.replace("]","],")
s2=s2[:-3]
s1+s2+s3

# import re

import requests 
import json
# defining the api-endpoint  
API_ENDPOINT = " http://localhost:9002/v1/models/mnist_experiments:predict"


#curl  -X POST http://localhost:8501/v1/models/half_plus_two:predict  -d '{\"instances\": [1.0, 2.0, 5.0]}'
# data to be sent to api 

data = {'instances':[[[[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [4.61361015e-05],        [2.76816609e-04],        [2.76816609e-04],        [2.76816609e-04],        [1.93771626e-03],        [2.09150327e-03],        [2.69127259e-03],        [3.99846213e-04],        [2.55286428e-03],        [3.92156863e-03],        [3.79853902e-03],        [1.95309496e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [4.61361015e-04],        [5.53633218e-04],        [1.44559785e-03],        [2.36831988e-03],        [2.61437908e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.46020761e-03],        [2.64513649e-03],        [3.89081123e-03],        [3.72164552e-03],        [2.99884660e-03],        [9.84236832e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [7.53556324e-04],        [3.66013072e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.86005383e-03],        [1.43021915e-03],        [1.26105344e-03],        [1.26105344e-03],        [8.61207228e-04],        [5.99769319e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.76816609e-04],        [3.36793541e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.04498270e-03],        [2.79892349e-03],        [3.79853902e-03],        [3.70626682e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [1.23029604e-03],        [2.39907728e-03],        [1.64552095e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.15263360e-03],        [1.69165705e-04],        [0.00000000e+00],        [6.61284121e-04],        [2.36831988e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.15301807e-04],        [1.53787005e-05],        [2.36831988e-03],        [3.89081123e-03],        [1.38408304e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.13763937e-03],        [3.89081123e-03],        [2.92195309e-03],        [3.07574010e-05],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [1.69165705e-04],        [2.92195309e-03],        [3.89081123e-03],        [1.07650903e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [5.38254517e-04],        [3.70626682e-03],        [3.46020761e-03],        [2.46059208e-03],        [1.66089965e-03],        [1.53787005e-05],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [1.24567474e-03],        [3.69088812e-03],        [3.89081123e-03],        [3.89081123e-03],        [1.83006536e-03],        [3.84467512e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [6.92041522e-04],        [2.86043829e-03],        [3.89081123e-03],        [3.89081123e-03],        [2.30680507e-03],        [4.15224913e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.46059208e-04],        [1.43021915e-03],        [3.87543253e-03],        [3.89081123e-03],        [2.87581699e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [3.82929642e-03],        [3.89081123e-03],        [3.82929642e-03],        [9.84236832e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [7.07420223e-04],        [1.99923106e-03],        [2.81430219e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.18339100e-03],        [3.07574010e-05],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [5.99769319e-04],        [2.27604767e-03],        [3.52172241e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.84467512e-03],        [2.79892349e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [3.69088812e-04],        [1.75317186e-03],        [3.39869281e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.09111880e-03],        [1.19953864e-03],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [3.53710111e-04],        [1.01499423e-03],        [3.27566321e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.04498270e-03],        [1.24567474e-03],        [3.07574010e-05],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.76816609e-04],        [2.62975779e-03],        [3.36793541e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [2.99884660e-03],        [1.23029604e-03],        [1.38408304e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [8.45828527e-04],        [2.64513649e-03],        [3.47558631e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.75240292e-03],        [2.04536717e-03],        [1.69165705e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [2.09150327e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.89081123e-03],        [3.26028451e-03],        [2.07612457e-03],        [2.02998847e-03],        [2.46059208e-04],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]],       [[0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00],        [0.00000000e+00]]]]}

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = json.dumps(data)) 
# extracting response text
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)