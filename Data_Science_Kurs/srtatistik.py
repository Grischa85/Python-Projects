import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')
df_EU_JP = df[["EU_Sales","JP_Sales"]]
df_JP = df["JP_Sales"]
print()

df.groupby("Year").agg(
    mean = ("NA_Sales", np.mean),
    median = ("NA_Sales", np.median),
    minimum = ("NA_Sales", np.min),
    maximum = ("NA_Sales", np.max),
)

df_groupby = df.groupby("Year").agg(
    mean = ("NA_Sales", np.mean),
    median = ("NA_Sales", np.median),
    minimum = ("NA_Sales", np.min),
    maximum = ("NA_Sales", np.max),
)

print(df_groupby)


df_groupby.plot()
plt.show()