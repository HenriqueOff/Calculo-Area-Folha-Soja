import cv2
import numpy as np

# Função para carregar a imagem com tratamento de erro
def carregar_imagem(nome_arquivo):
    try:
        imagem = cv2.imread(nome_arquivo)
        if imagem is None:
            raise FileNotFoundError("Não foi possível ler o arquivo {}".format(nome_arquivo))
        return imagem
    except Exception as e:
        print("Erro ao carregar a imagem:", e)
        return None

# Função para aplicar filtro e detectar a parte verde da imagem
def detectar_verde(imagem):
    # Converter imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Definir intervalo de cor verde (em HSV)
    lower_green = np.array([36, 25, 25])
    upper_green = np.array([86, 255, 255])

    # Criar máscara para identificar pixels verdes
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Aplicar a máscara na imagem original para visualizar apenas a parte verde
    parte_verde = cv2.bitwise_and(imagem, imagem, mask=mask)

    return parte_verde

# Função para pintar a parte verde da imagem de vermelho
def pintar_verde_com_vermelho(imagem):
    # Converter imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar um filtro de limiarização para destacar a parte verde
    _, imagem_limiarizada = cv2.threshold(imagem_cinza, 10, 255, cv2.THRESH_BINARY)

    # Pintar a região verde de vermelho
    imagem[imagem_limiarizada > 0] = [0, 0, 255]

    return imagem

# Função para calcular a área da parte vermelha da imagem
def calcular_area_vermelha(imagem):
    # Converter imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar um filtro de limiarização para identificar a parte vermelha
    _, imagem_limiarizada = cv2.threshold(imagem_cinza, 10, 255, cv2.THRESH_BINARY)

    # Calcular a área da parte vermelha da imagem
    area_vermelha = cv2.countNonZero(imagem_limiarizada)

    return area_vermelha

# Função para calcular a área real (em centímetros quadrados) da parte vermelha da imagem
def calcular_area_vermelha_cm2(imagem, proporcao_pixels_por_cm):
    # Calcular a área da parte vermelha da imagem em pixels
    area_vermelha_pixels = calcular_area_vermelha(imagem)
    
    # Calcular a área real (em centímetros quadrados) utilizando a proporção de pixels por centímetro
    area_vermelha_cm2 = area_vermelha_pixels / (proporcao_pixels_por_cm ** 2)
    
    return area_vermelha_cm2

# Proporção de pixels por centímetro
proporcao_pixels_por_cm = 24.4  # 24.4 pixels/cm

# Carregar a primeira imagem (folha_antes.jpg)
imagem_antes = carregar_imagem('folha_antes.jpg')

# Verificar se a imagem foi carregada corretamente
if imagem_antes is None:
    print("Não foi possível carregar a imagem folha_antes.jpg. Verifique o arquivo de imagem.")
else:
    # Detectar a parte verde da imagem
    parte_verde_antes = detectar_verde(imagem_antes)

    # Pintar a parte verde da imagem de vermelho
    parte_verde_pintada_antes = pintar_verde_com_vermelho(parte_verde_antes)

    # Calcular a área da parte vermelha da imagem
    area_vermelha_antes = calcular_area_vermelha(parte_verde_pintada_antes)

    # Calcular a área real da parte vermelha da imagem
    area_vermelha_antes_cm2 = calcular_area_vermelha_cm2(parte_verde_pintada_antes, proporcao_pixels_por_cm)

    # Exibir a área da parte vermelha da imagem
    print("Área da parte vermelha da imagem (antes):", area_vermelha_antes, "pixels")
    print("Área real da parte vermelha da imagem (antes):", area_vermelha_antes_cm2, "cm^2")

# Carregar a segunda imagem (folha_depois.jpg)
imagem_depois = carregar_imagem('folha_depois.jpg')

# Verificar se a imagem foi carregada corretamente
if imagem_depois is None:
    print("Não foi possível carregar a imagem folha_depois.jpg. Verifique o arquivo de imagem.")
else:
    # Detectar a parte verde da imagem
    parte_verde_depois = detectar_verde(imagem_depois)

    # Pintar a parte verde da imagem de vermelho
    parte_verde_pintada_depois = pintar_verde_com_vermelho(parte_verde_depois)

    # Calcular a área da parte vermelha da imagem
    area_vermelha_depois = calcular_area_vermelha(parte_verde_pintada_depois)

    # Calcular a área real da parte vermelha da imagem
    area_vermelha_depois_cm2 = calcular_area_vermelha_cm2(parte_verde_pintada_depois, proporcao_pixels_por_cm)

    # Exibir a área da parte vermelha da imagem
    print("Área da parte vermelha da imagem (depois):", area_vermelha_depois, "pixels")
    print("Área real da parte vermelha da imagem (depois):", area_vermelha_depois_cm2, "cm^2")
    
    # Exibir a imagem com a parte verde pintada de vermelho
    #cv2.imshow('Parte verde Pintada de vermelho (Antes)', parte_verde_pintada_antes)
    #cv2.imshow('Parte Verde Pintada de Vermelho (Depois)', parte_verde_pintada_depois)
    #cv2.waitKey(0)# Aguardar a tecla ser pressionada para fechar a janela
    
    # Salvar a imagem temporária
    cv2.imwrite('parte_verde_pintada_antes.jpg', parte_verde_pintada_antes)
    cv2.imwrite('parte_verde_pintada_depois.jpg', parte_verde_pintada_depois)

    # Abrir as imagens usando o visualizador padrão do sistema
    import subprocess
    subprocess.run(['xdg-open', 'parte_verde_pintada_antes.jpg'])
    subprocess.run(['xdg-open', 'parte_verde_pintada_depois.jpg'])

    

    
