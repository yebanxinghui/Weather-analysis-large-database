import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fileName = 'E:/课件/大数据/经纬度聚类.csv'
frame = pd.read_csv(fileName,engine='python')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
colors = ['g','r','y','b']
markers = ['o','s','d','h']
for i in range(3000):
    plt.plot(frame["经度"][i],frame["纬度"][i],color=colors[frame["聚类"][i]],marker=markers[frame["聚类"][i]],ls='None')
plt.title('所有城市八年来天气情况聚类')
plt.grid()
plt.show()
