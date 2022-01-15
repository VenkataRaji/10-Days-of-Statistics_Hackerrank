"""Import pandas as it has in-built easy to use mean,median and mode functions
(measures of central tendency)"""
import pandas as pd


n=int(input())
l=list(map(int,input().split(" ")))

#convert the python list l as pandas series s
s=pd.Series(l)

#print mean,median and mode
print(round(s.mean(),1))
print(round(s.median(),1))
md=s.mode()
print(round(md.min(),1))
