import pandas as pd
import plotly.express as px

df = pd.read_csv("cases_data.csv")
fig = px.line(df,x="date",y="cases",color="country",title="Number of cases of COVID-19")
fig.show()