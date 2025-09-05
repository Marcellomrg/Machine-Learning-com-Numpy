# %%
import numpy as np

# %%
x1  = np.array([2,8,11,10,8,4,2,2,9,8])
# %%
x2 = np.array([50,110,120,550,295,
               200,375,52,100,300])
# %%
y = np.array([9.95,24.45,31.75,
              35,25.02,16.86,
              14.38,9.6,24.35,
              27.5])

# %%
X = np.column_stack((np.ones(len(x2)),x1,x2))
print(X)
# %%
X_T = X.transpose()
X_T
# %%
beta = np.linalg.inv(X_T @ X) @ (X_T @ y)
beta 
# %%
# Intercepto (beta_0)
# # -> indica o valor de y quando x for 0
# coeficiente angulares indicam
# quando y muda para cada unidade de x

y_pred = X @ beta
ss_total = np.sum((y-y.mean())**2)
ss_residuos = np.sum((y - y_pred)**2)
r_score = 1 - ss_residuos / ss_total
print(r_score)
# %%
equacao = f"y = {beta[0]:.3f} + {beta[1]:.3f}*x1 + {beta[2]:.3f}*x2"
equacao
# %%
y = 4.544 + 2.216*x1 + 0.015*x2
print(y)
# %%
novos_x1 = np.array([2,5,10,15])
novos_x2 = np.array([2,100,200,300])
y_pred_equacao = []

for i in range(len(novos_x1)):
    y_pred = beta[0] + beta[1]*novos_x1[i] + beta[2] *novos_x2[i]
    y_pred_equacao.append(y_pred)
# %%
y_pred_equacao
# %%
