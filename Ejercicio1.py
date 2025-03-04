import numpy as np

candidatos = 30
estudiantes = 5000

votos = np.random.randint(1, candidatos + 1, estudiantes)

conteo = np.zeros(candidatos, dtype=int)
for voto in votos:
    conteo[voto - 1] += 1

candidatos = np.arange(1, candidatos + 1)
resultados = np.column_stack((candidatos, conteo))

resultados = resultados[resultados[:, 1].argsort()[::-1]]

print("Listado de votos obtenidos :")
for candidato, votos in resultados:
    print("Candidato ",candidato, ":", votos, "votos")
