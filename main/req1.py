import models.classes as c
import dao.functions as f
import datetime
 
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
            elif opcion == 5:
                registrar_pago()
            elif opcion == 4:
               eliminar_cliente() 
            elif opcion == 8:
                print("En proceso de mejora")
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
    
    #agregando cédula como identificador
    while True:
        try:
            cedula_str = input("Ingrese la cédula del cliente [Formato = xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]: ").strip()
            if (len(cedula_str) == 16 and cedula_str[3] == '-' and cedula_str[10] == '-' and cedula_str[:-1].replace('-', '').isdigit() and cedula_str[-1].isalpha()):
                break
            else:
                print("Numero de cédula inválido. El formato introducido es inválido")
        except ValueError:
            print("Caracteres inválidos. Por favor, solo ingrese el formato adecuado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        
            
    while True:
        try:
            numero_telefono_str = input("Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación]: ") 
            if len(numero_telefono_str) == 8 and numero_telefono_str.isdigit():
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
            
    registrar = c.Client(nombres, apellidos, cedula_str ,numero_telefono, correo_elec, direccion, plan)
    servicios.add(registrar)
    
#def buscar_facturas():
#    #NOTA: Ahorita no hay creación de factura automática, por lo que solo haré que busque el nombre e imprima el plan
#    while True:
#           try:
#               busqueda = input("Ingrese los 2 nombres o los 2 apellidos del cliente a buscar: ").strip()
#               if all(part.isalpha() for part in busqueda.split()):
#                   found = False
#                   for cliente in servicios.service:
#                       if cliente.name == busqueda or cliente.last_name == busqueda:
#                           print(cliente)  
#                           found = True
#                           break
#                   if not found:
#                       print("El usuario que usted busca no existe o no fue introducido tal como fue guardado")
#               else:
#                   print("Caracter inválido, ingrese solo carácteres alfabéticos")
#           except ValueError:
#               print("Caracter inválido, ingrese solo carácteres alfabéticos")
               
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
               busqueda = input("Ingrese los 2 nombres, los 2 apellidos del cliente a buscar o la cedula: ").strip()
               if busqueda:
                   found = False
                   for cliente in servicios.service:
                       if cliente.name == busqueda or cliente.last_name == busqueda or cliente.identification == busqueda:
                        found = True
                        print("Cliente encontrado:")
                        print(cliente)
                        editar_nuevo_cliente(cliente)
                        break
                   if found:
                       break
                   else:
                       print("El usuario que usted busca no existe o no fue introducido tal como fue guardado")
               else:
                   print("Caracter inválido, ingrese solo carácteres alfabéticos")
           except ValueError:
               print("Caracter inválido, ingrese solo carácteres alfabéticos")


def editar_nuevo_cliente(cliente):
    #Aqui es copiar la estructura base de registrar_cliente para la validacción de datos
    while True:
        try:
            nuevo_nombre = input("Ingrese los 2 nuevos nombres del cliente: ").strip()
            if nuevo_nombre == "":
                break #Agregue esto si quiero mantener el nombre igual, ahora es agregar a todos
            elif  all(part.isalpha() for part in nuevo_nombre.split()):
                cliente.name = nuevo_nombre
                break
            else:
                print("Los nombres solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Error, caracteres inválidos")
        
        
    while True:
        try:
            nuevo_apellido = input("Ingrese los 2 nuevos apellidos del cliente: ")
            if nuevo_apellido == "":
                break
            elif  all(part.isalpha() for part in nuevo_apellido.split()):
                cliente.last_name = nuevo_apellido
                break
            else:
                print("Los apellidos solo deben contener caracteres alfabéticas")
        except ValueError:
            print("Caracter inválido, ingrese solo carácteres alfabéticos")
        
    while True:
        try:
            nueva_cedula = input("Ingrese la nueva cedula del cliente en [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]: ")
            if nueva_cedula == "":
                break
            elif len(nueva_cedula) == 16 and nueva_cedula[3] == '-' and nueva_cedula[10] == '-' and nueva_cedula[:-1].replace('-', '').isdigit() and nueva_cedula[-1].isalpha():
                break
            else:
                print("La nueva cédula no sigue el formato indicado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        except ValueError:
            print("Caracteres inválidos, por favor ingrese el formato adecuado [Formato: xxx-xxxxxx-xxxx, 13 números y caracter alfabético al final]")
        
    while True:
        try:
            nuevo_numero_telefono = input("Ingrese el número telefónico del cliente [8 dígitos, sin espacios de separación]: ") 
            if nuevo_numero_telefono == "":
                break
            elif len(nuevo_numero_telefono) == 8 and nuevo_numero_telefono.isdigit():
                cliente.phone_number = int(nuevo_numero_telefono)
                break
            else:
                    print("Numero de telefono inválido. Debe de ser de 8 números y sin espacios")
        except ValueError:
                print("Carácteres inválidos. Por favor, solo ingrese numeros")
                
    nuevo_correo_elec = input("Ingrese el nuevo correo electrónico del cliente: ").strip()
    if nuevo_correo_elec:
        cliente.email = nuevo_correo_elec
        
    nuevo_direccion = input("Ingrese la nueva dirección del cliente: ").strip()
    if nuevo_direccion:
        cliente.address = nuevo_direccion
                
    while True:
        nuevo_plan = input("Ingrese el nuevo plan elegido por el cliente [1 = Plan básico, 2 = Plan Pro, 3 = Plan Premium]: ")
        if nuevo_plan == "":
                break     
        try:
            nuevo_plan = int(nuevo_plan)
            if 1 <= nuevo_plan <= 3:
                if nuevo_plan == 1:
                    nuevo_plan = "Básico"
                elif nuevo_plan == 2:
                    nuevo_plan = "Pro"
                elif nuevo_plan == 3:
                    nuevo_plan = "Premium"
                cliente.plan = nuevo_plan
                break
            else:
                print("Por favor, ingrese un numero del 1 al 3")
        except ValueError:
            print("Carácteres inválidos. Por favor, solo ingrese un numero del 1 al 3")
            
    print("Cliente actualizado con éxito.")
    
def registrar_pago(cliente):
    while True:
        try:
            buscar = input("")
        except ValueError:
            print("No hay nada, solo estoy probando")