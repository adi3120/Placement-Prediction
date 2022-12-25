import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv("placement.csv")

df=df[["BRANCH","PLACED"]]

# df["PLACED"]=df["PLACED"].apply(lambda x: 1 if x==0 else 0)

df=df.groupby(['BRANCH']).sum()

x=["CS","IT","EE","ECE","E","MECH","CIVIL","OTHER"]

plt.bar(x,df["PLACED"])

plt.show()
