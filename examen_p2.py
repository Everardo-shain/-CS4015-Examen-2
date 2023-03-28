# Generación de Histogramas
import numpy as np
import sympy as sp 
import math
from matplotlib import pyplot as plt
# Instalar el paquete scipy si es necesario (Tools -> Manage Packages...)
import scipy.stats
#Carga de datos
data_estatura = np.loadtxt("estatura.txt", dtype=float)
data_talla = np.loadtxt("talla.txt", dtype=float)
estatura = np.array(data_estatura[:])
talla = np.array(data_talla[:])
clases = 8
rango_estatura = (87,189)
rango_talla = (22.5,30)
plt.figure(1)
plt.title("Histograma Estatura")
plt.xlabel("Estatura (cm)")
plt.hist(estatura, range=rango_estatura, bins = clases, density=False)
plt.figure(2)
plt.title("Histograma Talla")
plt.xlabel("Talla de calzado")
plt.hist(talla, range=rango_talla, bins = clases, density=False)

media_est=sum(estatura)/len(estatura)
media_tal=sum(talla)/len(talla)
desv_est=np.std(estatura)
desv_tal=np.std(talla)
print("Media aritmética de estatura: ", round(media_est,4))
print("Desviación estandar de estatura: ",round(desv_est,4))
print("Media aritmética de talla: ", round(media_tal,4))
print("Desviación estandar de talla: ",round(desv_tal,4))
x = np.linspace(0, 300, 400)
y = np.linspace(0, 40, 100)
def f1(x):
    return 1/(desv_est*math.sqrt(2*math.pi))*math.e**(-((x-media_est)**2)/(2*(desv_est**2)))
def f2(y):
    return 1/(desv_tal*math.sqrt(2*math.pi))*math.e**(-((y-media_tal)**2)/(2*(desv_tal**2)))
plt.figure(3)
plt.title("Función gaussiana Estatura")
plt.xlabel("Estatura")
plt.plot(x, f1(x), color='red')
plt.figure(4)
plt.title("Función gaussiana Talla")
plt.xlabel("Talla")
plt.plot(y, f2(y), color='red')
plt.show()


scipy.stats.norm(loc=media_est, scale=desv_est)
prob_est=scipy.stats.norm.cdf(media_est+desv_est,media_est,desv_est)-scipy.stats.norm.cdf(media_est-desv_est,media_est,desv_est)
print("Probabilidad de que una persona tomada al azar se encuentre dentro de la primera desviación estándar para estatura: ", round(prob_est,4))
scipy.stats.norm(loc=media_tal, scale=desv_tal)
prob_tal=scipy.stats.norm.cdf(media_tal+desv_tal,media_tal,desv_tal)-scipy.stats.norm.cdf(media_tal-desv_tal,media_tal,desv_tal)
print("Probabilidad de que una persona tomada al azar se encuentre dentro de la primera desviación estándar para talla: ", round(prob_tal,4))
    




