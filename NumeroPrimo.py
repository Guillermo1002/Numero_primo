def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
no_primos = []
for numero in range(1, 101):
    if es_primo(numero):
        primos.append(numero)
    else:
        no_primos.append(numero)

def mostrar_menu():
    print("MENÚ:")
    print("1. Ver lista de números primos del 1 al 100")
    print("2. Ver lista de números no primos del 1 al 100")
    print("3. Ver ambos listados")
    print("4. Ver si un número es primo")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        print("Números primos del 1 al 100:")
        print(primos)
    elif opcion == "2":
        print("Números no primos del 1 al 100:")
        print(no_primos)
    elif opcion == "3":
        print("Primos:", primos)
        print("No primos:", no_primos)
    elif opcion == "4":
        try:
            num = int(input("Ingrese un número para verificar si es primo: "))
            if es_primo(num):
                print(f"{num} ES un número primo.")
            else:
                print(f"{num} NO es un número primo.")
        except ValueError:
            print("Por favor, introduzca un número válido.")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.")
        
def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
    return True

lista_numeros_primos = []
lista_numeros_no_primos = []
for i in range(1, 101):
    if es_primo(i):
        lista_numeros_primos.append(i)
    else:
        lista_numeros_no_primos.append(i)
print(lista_numeros_primos)
print(lista_numeros_no_primos)

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i==0:
            return False
        return True
    print(es_primo(11))
    print(es_primo(12))
    print(es_primo(13))
    print(es_primo(14))
    print(es_primo(15))
    print(es_primo(16))
    print(es_primo(17))
    for i in range(1, 101):
        if es_primo(i):
            print(i)
        else:
            print(f"{i} no es primo")
    print("Fin del programa")
