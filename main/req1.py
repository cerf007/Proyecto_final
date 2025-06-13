import models.classes as c
import dao.functions as f
 
servicios = f.ServiceDao()

def menu():
    print("""
          Bienvenido a su registradora. ELija de una de las siguientes ipciones
          1.Agregar cliente
          2.Mostrar clientes
          3.Registrar pagos
          4.Editar clientes 
          5.Generar reporte financiero
          6.Impresión de facturas
          7.Busqueda de facturas
          8.Salir
          """)
    
def main():
    while True:
        try:
            menu()
            opcion = int(input("Ingrese la opcion: ")) #Se me olvido el input
            if opcion == 1:
                registrar_cliente()
            elif opcion == 2:
                servicios.show()
            else:
                print("Opción inválida. Ingrese solo el número 1 por ahora")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


    

def registrar_cliente():
    nombres = input("Ingrese los 2 nombres del cliente: ").strip()
    apellidos = input("Ingrese los 2 apellidos del cliente: ").strip()
    while True:
        try:
            numero_telefono_str = input("Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación]: ") 
            if len(numero_telefono_str) == 8 and numero_telefono_str.isdigit:
                numero_telefono = int(numero_telefono_str)
                break
            else:
                print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese numeros")
            
    correo_elec = input("Ingrese el correo electrónico del cliente: ").strip()
    direccion = input("Ingrese la dirección del cliente: ").strip()
    while True:
        try:
            plan = int(input("Ingrese el plan elegido por el cliente [1 = Plan básico, 2 = Plan Pro, 3 = Plan Premium]: "))
            
            if 1 <= plan <= 3:
                break
            else:
                print("Por favor, ingrese un numero del 1 al 3")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese un numero del 1 al 3")
            
    registrar = c.Service(nombres, apellidos, numero_telefono, correo_elec, direccion, plan)
    servicios.add(registrar)
    