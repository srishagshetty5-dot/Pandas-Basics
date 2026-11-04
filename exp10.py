# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:48:35 2026

@author: user
"""

import pandas as pd
data={
      "name":["A","B","C","D"],
      "marks":[80,90,85,70],
      "age":[25,54,43,21],
      "rollno":[567,798,400,343],
      
      }
df=pd.DataFrame(data)
print(df)
print("Head:\n",df.head())
print("\nTail:\n",df.tail())
print("\ninfo:")
df.info()
print("\ndescribe:\n",df.sort_values("marks"))
print("\nsorted:",df.sort_values("rollno"))

