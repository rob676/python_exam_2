from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: якого товару на яку суму продано.
data = dict(recursionByAutomobiles())
print(data)

diagram =go.Pie (
    values=list(data.keys()),
    labels=list(data.values())
)

plotly.offline.plot(go.Figure[diagram],filename='task5.html')