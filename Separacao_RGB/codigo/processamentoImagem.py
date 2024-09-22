import cv2
import numpy as np

# Carregar a imagem 
imagem = cv2.imread('images\\cavalo.jpg')

if imagem is None:
    print("Erro ao carregar a imagem.")

# Separando os canais de cor em azul, verde e vermelho
azul, verde, vermelho = cv2.split(imagem)

# Mesclando os canais de cor, na ordem azul, verde e vermelho
imagem_mesclada = cv2.merge((azul, verde, vermelho))

# Invertendo os canais de cor 
imagem_invertida = cv2.merge((vermelho, verde, azul))

# Criando uma imagem branca nas dimensões da imagem lida 
blank = np.zeros(imagem.shape[:2], dtype='uint8')

# Abrindo as imagens por canais e mesclando com as matrizes de zeros
canal_azul = cv2.merge([azul,blank,blank])
canal_verde = cv2.merge([blank,verde,blank])
canal_vermelho = cv2.merge([blank,blank,vermelho])

# Visualizando
cv2.imwrite('Azul.png', canal_azul)
cv2.imwrite('Verde.png', canal_verde)
cv2.imwrite('Vermelho.png', canal_vermelho)

cv2.imwrite('imagem_mesclada.png', imagem_mesclada)
cv2.imwrite('imagem_invertida.png', imagem_invertida)
