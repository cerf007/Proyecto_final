import models.classes as c
import dao.functions as f
 
servicios = f.ClientDao()

def menu():
    print("""
          Bienvenido a su registradora. ELija de una de las siguientes ipciones
          1.Agregar cliente
          2.Mostrar clientes
          3.Editar clientes
          4.Eliminar Cliente
          5.Registrar pagos
          6.Generar reporte financiero
          7.Impresión de facturas
          8.Busqueda de facturas
          9.Salir
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
            elif opcion == 3:
                editar_cliente()
            elif opcion == 4:
               eliminar_cliente() 
            elif opcion == 8:
                buscar_facturas()
            else:
                print("Opción inválida. Ingrese solo el número 1 por ahora")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


    

def registrar_cliente():
    while True:
        try:
            nombres = input("Ingrese los 2 nombres del cliente: ").strip()
            if all(part.isalpha() for part in nombres.split()):
                break
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Error, caracteres inválidos")
            
    while True:
        try:
            apellidos = input("Ingrese los 2 apellidos del cliente: ").strip()
            if all(part.isalpha() for part in apellidos.split()):
                break
            else:
                print("Los apeellidos solo deben de contener caracteres alfabéticos ")
        except  ValueError:
            print("Error, caracteres inválidos")
            
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
                if plan == 1:
                    plan = "Básico"
                elif plan == 2:
                    plan = "Pro"
                elif plan == 3:
                    plan = "Premium"
                break
            else:
                print("Por favor, ingrese un numero del 1 al 3")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese un numero del 1 al 3")
            
    registrar = c.Client(nombres, apellidos, numero_telefono, correo_elec, direccion, plan)
    servicios.add(registrar)
    
def buscar_facturas():
    #NOTA: Ahorita no hay creación de factura automática, por lo que solo haré que busque el nombre e imprima el plan
    while True:
           try:
               busqueda = input("Ingrese los 2 nombres o los 2 apellidos del cliente a buscar: ").strip()
               if all(part.isalpha() for part in busqueda.split()):
                   found = False
                   for cliente in servicios.service:
                       if cliente.name == busqueda or cliente.last_name == busqueda:
                           print(cliente)  
                           found = True
                           break
                   if not found:
                       print("El usuario que usted busca no existe o no fue introducido tal como fue guardado")
               else:
                   print("Caracter inválido, ingrese solo carácteres alfabéticos")
           except ValueError:
               print("Caracter inválido, ingrese solo carácteres alfabéticos")
               
def eliminar_cliente():
    while True:
        try:
            nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ").strip()
            client_to_delete = next((client for client in servicios.service if client.name == nombre_cliente), None)
            if client_to_delete:
                servicios.delete(client_to_delete)
                print(f"Cliente {nombre_cliente} eliminado.")
                break
            else:
                print("Cliente no encontrado.")
        except ValueError:
            print("Entrada no válida, intenté de nuevo")
            
def editar_cliente():
    #Decidi usar copiar y pegar la estructura base de la fución buscar_facturas (La función cambiara después)
     while True:
           try:
               busqueda = input("Ingrese los 2 nombres o los 2 apellidos del cliente a buscar: ").strip()
               if all(part.isalpha() for part in busqueda.split()):
                   found = False
                   for cliente in servicios.service:
                       if cliente.name == busqueda or cliente.last_name == busqueda:
                           
                           found = True
                           break
                   if not found:
                       print("El usuario que usted busca no existe o no fue introducido tal como fue guardado")
               else:
                   print("Caracter inválido, ingrese solo carácteres alfabéticos")
           except ValueError:
               print("Caracter inválido, ingrese solo carácteres alfabéticos")