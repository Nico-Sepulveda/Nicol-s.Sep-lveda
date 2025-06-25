entradas = {}

def validar_codigo(codigo):
    if len(codigo) < 6:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if " " in codigo:
        return False
    return True

def comprar_entrada():
    nombre = input("Ingresa el nombre del comprador: ")
    if nombre in entradas:
        print("Se registró el nombre del comprador.")
        return
    
    tipo = input("Tipo de entrada (G/V): ").upper()
    if tipo not in ["G", "V"]:
        print("Inválido. Solo se permite 'G' o 'V'.")
        return
    
    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar_codigo(codigo):
            entradas[nombre] = {"tipo": tipo, "codigo": codigo}
            print("Código validado. ¡Entrada registrada con éxito!")
            break
        else:
            print("Código no válido. Intente otra vez.")

def consultar_comprador():
    nombre = input("Ingrese nombre de comprador a buscar: ")
    if nombre in entradas:
        datos = entradas[nombre]
        print(f"Tipo de entrada: {datos['tipo']}, Código: {datos['codigo']}")
    else:
        print("El comprador no se encuentra.")

def cancelar_compra():
    nombre = input("Ingrese nombre de comprador a cancelar: ")
    if nombre in entradas:
        del entradas[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra.")

def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            consultar_comprador()
        elif opcion == "3":
            cancelar_compra()
        elif opcion == "4":
            print("Programa terminado.")
            break
        else:
            print("Debe ingresar una opción válida!")
main()