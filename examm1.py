lista = ["1", "2", "3", "4", "5", "6"]

def most_numerosss():
      print("Lista actual:", lista)


def agre_numero():

    nuevo_numero = input("Introduce el nuevo numero3: ")
    lista.append(nuevo_numero)
    print("La Lista ahora es:", lista)

def modificar_numeross():
    most_numerosss()
    indice = int(input("numerop que quieres modificar (0 para el primero): "))
    if indice >= 0 and indice < len(lista):

        nuevo_valor = input("Introduce el nuevo valor del numero: ")
        lista[indice] = nuevo_valor
        print("Numero modificado , la lista ahora es:", lista)
    else:
        print("invalido")


def eliminar_numero():
    most_numerosss()
    numero_a_eliminar = input("numero a eliminar: ")
    if numero_a_eliminar in lista:
        lista.remove(numero_a_eliminar)
        print("eliminado, ahora es:", lista)
    else:
        print("ese numero no esta en la lista")


while True:
    print("\n▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ")
    print("Opciones:")
    print("1. ver lista de numeros")
    print("2. Agregar un numero")
    print("3. modificar un número")
    print("4. Eliminar un número")
    print("5. Salir")
    print("▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ")

    opcion = input("\nSelecciona una opcion: ")

    if opcion == "1":
        most_numerosss()
    elif opcion == "2":
        agre_numero()
    elif opcion == "3":
        modificar_numeross()
    elif opcion == "4":
        eliminar_numero()
    elif opcion == "5":
        print("nos vemos...")
        break
    else:
        print("error, no valido")
