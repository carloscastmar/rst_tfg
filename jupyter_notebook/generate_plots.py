import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")


def gen_plot_for_latency(data_file):
    df = pd.read_csv(
        data_file + ".dat",
        skiprows=3,
        delimiter=r":\s+",
        header=None,
        usecols=[2],
        names=["latency"],
        engine="python"
    )

    latency_df = df.drop(df[df.latency < 4].index)

    print(data_file + ":")
    print(latency_df.describe())

    print(latency_df.value_counts())

    sns.displot(data=latency_df, x="latency", kind="kde")
    plt.savefig(data_file + "_dist_kde.png", dpi=300)

    sns.histplot(data=latency_df, x="latency", binwidth=1)
    plt.savefig(data_file + "_hist.png", dpi=300)


data_files = [
    "latency_serial_best-effort",
    "latency_serial_reliable",
    "latency_wifi_best-effort",
    "latency_wifi_reliable",
]

for data_file in data_files:
    gen_plot_for_latency(data_file)
