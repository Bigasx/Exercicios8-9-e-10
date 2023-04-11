def ler_temperatura():
   
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura
def calcular_temperatura_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5
    return temperatura_fahrenheit
def mostrar_resultado(temperatura_fahrenheit):
    print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}")

