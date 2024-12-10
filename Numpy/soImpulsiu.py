from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from pathlib import Path 

# Funció exercici 2.
def deteccioSoroll(imatgeContaminada, m, w, k):
    pass

# Funció exercici 1.
def obrirImatge(nomArxiu, percentatge=5):
    contador=0
    # Abrimos imagen, utilizamos la libreria PIL.
    imagenOriginal = Image.open(nomArxiu)

    # Convertimos la imagen a una matriz tridimensional
    matriu_imagenOriginal = np.array(imagenOriginal)

    # Creamos una copia de la imagen original donde aplicaremos el ruido
    matriu_corrupta = matriu_imagenOriginal.copy()

    # Imprimimos dimensiones de la imagen
    print(f"Imatge {nomArxiu} de dimensions {matriu_imagenOriginal.shape}")

    # Obtenemos dimensiones de la imagen
    alt, ample, profunditatColor = matriu_imagenOriginal.shape

    # Contaminamos toda la imagen excepto los bordes
    for i in range(1, alt - 1):
        for j in range(1, ample - 1):
            # Con un 5% de probabilidad, alteramos el píxel
            if random.randint(1, 100) < percentatge:
                contador += 1
                r = random.randint(1, 100)
                
                # Determinamos el valor a usar (0 o 255)
                extrem = 0 if r % 2 == 0 else 255

                if r < 10:
                    matriu_corrupta[i, j] = [extrem, extrem, extrem]
                elif r < 40:
                    matriu_corrupta[i, j, 0] = extrem
                elif r < 70:
                    matriu_corrupta[i, j, 1] = extrem
                else:
                    matriu_corrupta[i, j, 2] = extrem

    print(f"Píxeles contaminados: {contador}")

    # Mostramos la imagen contaminada
    plt.imshow(matriu_corrupta)
    plt.axis('off')
    plt.show()

    # Convertimos la matriz con ruido a imagen PIL
    imagen_corrupta = Image.fromarray(matriu_corrupta)

    # Creamos el nombre final para la imagen guardada
    nomSenseExtensio = Path(nomArxiu).stem
    nombre_final = f"{nomSenseExtensio}_{percentatge}.png"

    # Guardamos la imagen en el directorio donde se ejecuta el programa
    ruta_guardado = os.path.join(os.path.dirname(__file__), nombre_final)
    imagen_corrupta.save(ruta_guardado)
    print(f"Imatge contaminada guardada com: {ruta_guardado}")

if __name__ == "__main__":
    directorio_actual = os.path.dirname(__file__)
    archivo = os.path.join(directorio_actual, "pepino.jpg")
    obrirImatge(archivo, percentatge=5)
