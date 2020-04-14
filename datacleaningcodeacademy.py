import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
files = glob.glob("states*.csv")
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
df=pd.concat(df_list)
#print(df.columns)
df["Income"]=pd.to_numeric(df["Income"].replace("[$]","",regex=True))
m_f=df["GenderPop"].str.split("_")
df["Men"]=pd.to_numeric(m_f.str.get(0).replace("[M]","",regex=True))
df["Women"]=pd.to_numeric(m_f.str.get(1).replace("[F]","",regex=True))
df=df.fillna(value={"Women":df["TotalPop"]-df["Men"]})
#print(df.duplicated().value_counts())
df.drop_duplicates()
#plt.scatter(df["Women"],df["Income"])
#plt.show()
df = pd.melt(frame=df,id_vars=["State","TotalPop","Income","Men","Women"],value_vars=["Hispanic","White","Black","Native","Asian","Pacific"],value_name="Percentage",var_name="Race")
df["Percentage"]=pd.to_numeric(df["Percentage"].replace("[%]","",regex=True))