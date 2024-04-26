import plotly.express as px

def sample_plot(x, y):
    fig = px.bar(x=x,y=y)
    fig.show()