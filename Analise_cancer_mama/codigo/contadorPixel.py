import cv2
import numpy as np
img = cv2.imread('semana 5/mama_contornos.jpg')
#cv2.inshow('image', img)
numero_pixels_branco = np.sum(img == 255)
numero_pixels_preto = np.sum(img == 0)

print('Numero de pixels brancos:', numero_pixels_branco)
print('Numero de pixels pretos:', numero_pixels_preto)

# Calcula a media dos pixels brancos 
percentual_pixels_brancos = numero_pixels_branco / (numero_pixels_branco + numero_pixels_preto) * 100

print('Percentual de pixels brancos:', percentual_pixels_brancos)
if (percentual_pixels_brancos >= 30):
    print('Imagem com cancer')
else:
    print('Imagem sem cancer')