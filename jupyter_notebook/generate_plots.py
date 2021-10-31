import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

df= pd.read_csv("latency_serial_best-effort.dat",skiprows=3,delimiter=r":\s+",header=None,usecols=[2],names=['latency'])

latency_sbe= df.drop(df[df.latency < 4].index)

latency_sbe.describe()

latency_sbe.value_counts()

sns.displot(data=latency_sbe,x="latency",kind="kde")
plt.savefig('latency_sbe_kde.png', dpi=300)

sns.histplot(data=latency_sbe,x="latency",binwidth=1)
plt.savefig('latency_sbe_hist.png', dpi=300)

