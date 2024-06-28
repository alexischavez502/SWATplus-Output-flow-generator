# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:21:30 2024

@author: ALEXIS
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

#Verificar el directorio actual
directory= os.getcwd()
print(directory)

#Change directory of TxtInOut
##Type the directory
os.chdir(r"C:\Users\ALEXIS\Documents\QGIS\SWAT_of\ENDE_CORANI\Scenarios\Cambio_Climatico\TxtInOut")
#skiping rows
# Read the file
model='Control_reevaluation_daily'
data=pd.read_csv("channel_sdmorph_day.txt", header=None,
                   skiprows=1,sep=r"\s+",decimal='.', 
                   usecols=[1,2,3,4,5,6,7,8,9,10],low_memory=False)
data.columns=data.iloc[0]
data=data[1:]
print("Total rows: {0}".format(len(data)))
print(data[:10])


# To filter from reach outlet
flowsim=data[data['name']=='cha054']
#For monthly
#flowout=pd.DataFrame().assign(mon=flowsim.mon,year=flowsim.yr,
#                              flo_in=flowsim.flo_in,flo_out=flowsim.flo_out).astype(float)
#For daily
flowout=pd.DataFrame().assign(day=flowsim.day,mon=flowsim.mon,year=flowsim.yr,
                              flo_in=flowsim.flo_in,flo_out=flowsim.flo_out).astype(float)
plt.plot(flowout.flo_in)
#extract to directory
out=(r'D:\UPWORK_FREELANCE\CORANI\03_Planillas\03_Caudales\Salida_swat\Perturbed\RCP85\M8')
flowout.to_excel(out+'/cha054'+model+'.xlsx',index=False)


