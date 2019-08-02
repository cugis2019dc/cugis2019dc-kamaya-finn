#import all libraries needed
import pandas as pd
import plotly as plt
from plotly.offline import plot
import plotly.graph_objs as go

#to read exel file(pd.read_exel), insert file name 
#and then the name of the worksheet. 
#doing ths will import the info from an outside file
wodf=pd.read_excel('GISdata.xlsx', sheet_name='womenOccupation')

titles= go.Layout(title='Percentage of Women Employed by Occupation',
                 xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Occupation',)),
                 yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='Percentage',)))
                                                                   
#label x and y axis as well as setting the colorscales
womenoccupation=go.Bar(x=wodf['occupation'],y=wodf['women'],
                       marker={'color':wodf['women'],'colorscale':'solar'})
fig= go.Figure(data=[womenoccupation],layout=titles)
plot(fig)