# Lista de clientes con estados iniciales
clientes = [
    {"nombre": "Roger Sequeira", "estado": "Pendiente"},
    {"nombre": "Reynaldo Molina", "estado": "Pagada"},
    {"nombre": "Jose Cristo", "estado": "Vencida"},
    {"nombre": "Calos rodriguez", "estado": "Pendiente"}
]

# Diccionario para traducir opciones a estados
opciones_estado = {
    "1": "Pagada",
    "2": "Pendiente",
    "3": "Vencida",
    "4": "Moroso",
    "5": "Al día"
}

def ver_estado_cliente(nombre_cliente):
    for cliente in clientes:
        if cliente["nombre"].lower() == nombre_cliente.lower():
            return cliente["estado"]
    return None

def actualizar_estado_cliente(nombre_cliente, nuevo_estado):
    for cliente in clientes:
        if cliente["nombre"].lower() == nombre_cliente.lower():
            cliente["estado"] = nuevo_estado
            return True
    return False

def main():
    print("Bienvenido al sistema de estados de clientes.\n")

    while True:
        nombre = input("Por favor, ingresa tu nombre para consultar o actualizar tu estado (o escribe 'salir' para terminar): ").strip()
        if nombre.lower() == "salir":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        estado_actual = ver_estado_cliente(nombre)
        if estado_actual:
            print(f"Hola {nombre}, tu estado actual es: {estado_actual}")
            print("¿Quieres actualizar tu estado?")
            print("Opciones: 1 = Pagada, 2 = Pendiente, 3 = Vencida, 4 = Moroso, 5 = Al día")
            opcion = input("Selecciona el número correspondiente a tu nuevo estado, o presiona Enter para mantener el actual: ").strip()
            if opcion == "":
                print("Estado no modificado.\n")
            elif opcion in opciones_estado:
                nuevo_estado = opciones_estado[opcion]
                actualizado = actualizar_estado_cliente(nombre, nuevo_estado)
                if actualizado:
                    print(f"Estado actualizado a: {nuevo_estado}\n")
                else:
                    print("No se pudo actualizar el estado.\n")
            else:
                print("Opción inválida. Estado no modificado.\n")
        else:
            print(f"No se encontró un cliente con el nombre '{nombre}'. ¿Deseas agregarlo?")
            agregar = input("Escribe 's' para sí o cualquier otra tecla para no: ").strip().lower()
            if agregar == "s":
                print("Opciones de estado para asignar:")
                for key, val in opciones_estado.items():
                    print(f"{key} = {val}")
                opcion = input("Selecciona el número correspondiente al estado que quieres asignar: ").strip()
                if opcion in opciones_estado:
                    nuevo_estado = opciones_estado[opcion]
                    clientes.append({"nombre": nombre, "estado": nuevo_estado})
                    print(f"Cliente '{nombre}' agregado con estado '{nuevo_estado}'.\n")
                else:
                    print("Opción inválida. Cliente no agregado.\n")
            else:
                print("Cliente no agregado.\n")

if __name__ == "__main__":
    main()


