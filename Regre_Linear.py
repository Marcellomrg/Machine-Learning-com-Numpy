# %%
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
# %%
dataX = np.array([1,2,3])
dataX
# %%
datay = np.array([1,4,8])
datay
# %%
xbar = np.sum(dataX)/len(dataX)
xbar
# %%
ybar = np.sum(datay)/len(datay)
ybar
# %%
a = sum((dataX-xbar)*(datay-ybar))/sum((dataX-xbar)**2)
a
# %%
b = ybar - a * xbar
b
# %%
y_estimado = a * dataX + b
y_estimado
# %%
r_square = 1 - sum((datay - y_estimado)**2)/sum((datay - ybar)**2)
r_square
# %%
e = datay - y_estimado
e
# %%
Sqr = sum(e**2)
Sqr

# %%
px.scatter(dataX,datay,trendline="ols",labels={"x":"x","y":"y"})

# %%
