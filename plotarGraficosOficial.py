import matplotlib.pyplot as plt
import numpy as np

def desenharGrafico(titulo): 
  plt.xlabel("Comprimento de Onda [Å]")
  plt.ylabel("Intensidade [erg/sec/cm²]")
  plt.title(titulo)
  plt.show()

def plotar(titulo):
  x, y = np.loadtxt(titulo, delimiter = "  ", unpack = True)
  plt.plot(x, y, "k", linewidth=0.5)
  desenharGrafico(titulo)

def plotarTudo(titulos):
  for tituloAtual in titulos:
    plotar(tituloAtual)

arquivos = ["f1240_4381.dat", "f1245_888.dat", "f1308_5325.dat", "f1329_3262.dat", "f1558_4020.dat", "f1625_1688.dat"]

for i in range(len(arquivos)):
  print((i+1), "-", arquivos[i])
print((i+2), "-", "Plotar tudo")

n = int(input("Digite qual arquivo você quer plotar: "))
if(n == (i+2)):
  plotarTudo(arquivos)
else:
  plotar(arquivos[n-1])