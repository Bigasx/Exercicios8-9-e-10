def ler_valores():
   
    tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo_gasto, velocidade_media


def calcular_distancia(tempo_gasto, velocidade_media):
    
    distancia_percorrida = tempo_gasto * velocidade_media
    return distancia_percorrida


def calcular_litros_utilizados(distancia_percorrida):
   
    litros_utilizados = distancia_percorrida / 12
    return litros_utilizados


def apresentar_resultado(tempo_gasto, velocidade_media, distancia_percorrida, litros_utilizados):

    print(f"Tempo gasto: {tempo_gasto:.2f} horas")
    print(f"Velocidade média: {velocidade_media:.2f} km/h")
    print(f"Distância percorrida: {distancia_percorrida:.2f} km")
    print(f"Litros de combustível utilizados: {litros_utilizados:.2f} L")