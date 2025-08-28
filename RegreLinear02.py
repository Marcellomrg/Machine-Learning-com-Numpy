# %%
import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("data/slr06 (1) (1).csv",delimiter=",",skiprows=1)
dados
# %%
datax = dados[:,0]
datay = dados[:,1]
print(datax)
print(datay)
# %%
xbar = sum(datax)/len(datax)
ybar = sum(datay)/len(datay)
print(xbar)
print(ybar)

# %%
a = sum((datax - xbar) * (datay - ybar))/sum((datax - xbar)**2)
a
# %%
b = ybar - a * xbar
b
# %%
y_estimado  = a * datax + b
y_estimado
# %%
r_square = 1 - sum((datay - y_estimado)**2)/sum((datay -ybar)**2)
r_square
# %%
e = datay - y_estimado
sqr = sum(e**2)
print(e)
print(f"Minha soma dos quadrados dos residuos é {sqr}")
# %%
plt.figure(dpi=400)
plt.plot(datax,datay,"o")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(datax,y_estimado)
plt.legend(["Observados",f"y = {a:.3f}x + {b:.3f}"])
# %%
