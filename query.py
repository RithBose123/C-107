import csv
import pandas as pd
import plotly.graph_objects as go
id=input("give student id= ")
df=pd.read_csv("data.csv")
student_Df=df.loc[df["student_id"]==id]
print(student_Df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Scatter(
    x=student_Df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"]
))
fig.show()
