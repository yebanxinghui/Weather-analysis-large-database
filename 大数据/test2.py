import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def readcsv(fileName):
    weather = ['平均气温','温差','天气','风力','风向']
    data = pd.read_csv(fileName,header=None,names=weather,engine='python')
    return data

path = 'E:/课件/大数据/处理后/城市天气4.csv'
data = readcsv(path)

from sklearn.decomposition import PCA

def getPCAData(data,comp):
    pcaClf = PCA(n_components=comp, whiten=True)
    pcaClf.fit(data)
    data_PCA = pcaClf.transform(data) # 用来降低维度
    return data_PCA
    
def modiData(data):
    x1 = []
    x2=[]
    for i in range(0,len(data+1)):
        x1.append(data[i][0])
        x2.append(data[i][1])
    x1=np.array(x1)
    x2=np.array(x2)
    #重塑数据
    X=np.array(list(zip(x1,x2))).reshape(len(x1),2)
    return X
from sklearn.cluster import KMeans
def drawKmodel(XData,t):
    #解决中文显示问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure()
    colors = ['g','r','y','b']
    markers = ['o','s','d','h']
    kmeans_model = KMeans(n_clusters=t).fit(XData)
    for i,l in enumerate(kmeans_model.labels_):
        plt.plot(XData[i][0],XData[i][1],color=colors[l],marker=markers[l],ls='None')
    plt.title('所有城市八年来天气情况聚类')
    plt.show()

#标准化
from sklearn.preprocessing import StandardScaler
ss = StandardScaler();
data = ss.fit_transform(data)
dataPCA = getPCAData(data,2)
dataX = modiData(dataPCA)
drawKmodel(dataX,4)
