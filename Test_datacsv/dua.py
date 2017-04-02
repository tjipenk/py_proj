import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.tools.plotting import autocorrelation_plot
from mpi4py import MPI

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

file = sys.argv[1]
jenis = sys.argv[2]
data = pd.read_csv(file, index_col='tanggal', date_parser=dateparse)

dt = np.log(data[jenis])

dt.plot(label='Data '+jenis+' Pengamatan')
plt.savefig('grafik_'+jenis+'.png', transparent=False)
autocorrelation_plot(dt)
plt.savefig('grafik_autocorelation_'+jenis+'.png', transparent=False)
sm.graphics.tsa.plot_acf(dt, lags=40)
plt.savefig('grafik_acf_'+jenis+'.png', transparent=False)
sm.graphics.tsa.plot_pacf(dt, lags=40)
plt.savefig('grafik_pacf_'+jenis+'.png', transparent=False)
#ts.adfuller(dt, 1)
if MPI.COMM_WORLD.Get_rank()==0:
	arima_mod1 = sm.tsa.ARIMA(dt, (3,0,2)).fit(trend='nc' , disp = False)
print(arima_mod1.params)
#print (arima_mod1.params)
sm.stats.durbin_watson(arima_mod1.resid.values)
#ws.to_csv("Arima_resid"+jenis+".csv")
print(arima_mod1.aic)
print(arima_mod1.bic)
#print("HQIC: "+ arima_mod1.hqic)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax = arima_mod1.resid.plot(ax=ax);
resid1 = arima_mod1.resid
plt.savefig("Arima_Resid"+jenis+".png", transparent=False)

from datetime import datetime, timedelta

d = datetime(2014,8,1)
d2 = d + timedelta(days=1000)
sekarang = d.strftime("%Y-%m-%d")
terakhir = d2.strftime("%Y-%m-%d")
#if MPI.COMM_WORLD.Get_rank() == 0:
hasil = np.exp(arima_mod1.predict(sekarang,terakhir, dynamic=True))
hasil.to_csv("hasil"+jenis+".csv")
