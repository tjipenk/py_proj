import pandas as pd
#from sqlalchemy import create_engine
import statsmodels.api as sm
from multiprocessing import Pool
import multiprocessing
import sys

num_cores = multiprocessing.cpu_count()
#num_cores = int(sys.argv[2])
#infile = sys.argv[1]
infile = "data.csv";
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

data = pd.read_csv(infile, parse_dates=['tanggal'], date_parser=dateparse, index_col='tanggal')

x, y = data.shape
dataku =[a for a in range(y)]
mdl = [a for a in range(y)]
hasil = [a for a in range(y)]
hasilakhir = [a for a in range(y)]
kolom = ['suhumax.csv', 'suhumin.csv', 'precipitation.csv', 'wind.csv', 'kelembaban.csv', 'solar.csv']

def load_data(i):
    dt = data.iloc[:, i]
    return dt;


def processArima(data):
    model = sm.tsa.ARIMA(data, (2,0,2)).fit()  
    return model;
    
def processPredict(model):
    from datetime import datetime, timedelta
    d = datetime(2014, 8, 1)
    d2 = d+timedelta(days=1000)
    sekarang = d.strftime("%Y-%m-%d")
    terakhir = d2.strftime("%Y-%m-%d")
    hasil = model.predict(dynamic=True)
    return hasil;


def jalankan(masukan):
    mdl = processArima(masukan)
    hasil = processPredict(mdl)
    hasilakhir = hasil.to_frame()
    return hasilakhir

tasks =[]
results = []
if __name__ == "__main__":
    p = Pool(1)
    for i in range(y):
        out_list = list
        dataku[i] = load_data(i)
    
#    results = p.map(jalankan, (dataku[2], dataku[3], dataku[4], dataku[5], dataku[6], dataku[7]))
    #results = jalankan (dataku[2], dataku[3], dataku[4], dataku[5], dataku[6], dataku[7])
    results = jalankan(load_data(2))

    for i in range(5):
        outfile = "Par_%s.csv" % (kolom[i],)
        results[i].to_csv(outfile, header=False)
