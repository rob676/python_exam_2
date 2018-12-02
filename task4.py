from data import dataset
from task1 import addUserProduct
from task3 import recursionByAutomobiles
import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки отримав балів.

data = dict(recursionByAutomobiles())
print(data)

diagram =go.Bar (
    x=list(data.keys()),
    y=list(data.values())
)

plotly.offline.plot(go.Figure[diagram], filename='task4.html')