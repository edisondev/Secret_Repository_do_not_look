# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:56:33 2017

@author: Nick
"""

from sodapy import Socrata
import pandas as pd

import plotly
from plotly.graph_objs import Scatter, Layout

#for client with token:
#client = Socrata("sandbox.demo.socrata.com", "FakeAppToken", username="fakeuser@somedomain.com", password="ndKS92mS01msjJKs")
client = Socrata("data.calgary.ca", None)
results = client.get("qzer-3is5", order='date DESC', limit=2000) #get from website, date descending order, limit of 100 entries


#put into dataframe
results_df = pd.DataFrame.from_records(results)

#Data prep
results_df['date']=pd.to_datetime(results_df['date'])
#df.loc[df['major_incident_type'] == 'False Alarm']

#results_df['incident_count'].iloc(['major_incident_type'='False Alarm'])

#subset false alarm dataframe
fa_df=results_df.loc[results_df['major_incident_type'] == 'False Alarm']
f_df=results_df.loc[results_df['major_incident_type'] == 'Fire']

data1=Scatter(x=fa_df['date'],y=fa_df['incident_count'],name='False Alarm')
data2=Scatter(x=f_df['date'],y=f_df['incident_count'],name='Fire')

plotly.offline.plot({
    "data": [data1,data2],
    "layout": Layout(title="Calgary Fire Incidents",
                     legend=dict(orientation="h"))
})
