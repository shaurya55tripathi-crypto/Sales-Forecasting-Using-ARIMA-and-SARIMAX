import plotly.graph_objects as go
import dateutil
import pandas_ta_classic as pta   
import datetime

def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e1efff'
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b>"+str(i)[:10]+"<b>" for i in dataframe.columns],
            line_color='#0078ff', fill_color='#0078ff',
            align='center', font=dict(color='white', size=15), height=35,
        ),
        cells=dict(
            values=["<b>"+str(i)+"<b>" for i in dataframe.index]+[dataframe[i] for i in dataframe.columns],
            align='left', line_color=['white'], font=dict(color=['black'], size=15),
            fill_color=[[rowOddColor, rowEvenColor]*len(dataframe)]
        )
    )])
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
    return fig


