import pickle
import os
#Importa pickle para guardar objetos complejos en binario, y os para trabajar con archivos

class ClientDao:
    #Declara la clase encargada de manejar el almacenamiento de clientes
    def __init__(self):
        self.file_path = "clientes.bin" #ruta del archivo binario donde se guardarán los clientes
        self.service = self.load() #Carga con self.load() los clientes desde el archivo al arrancar el programa. Si no hay archivo, la lista queda vacía.
        
    def add(self, client):
        self.service.append(client)
        self.save()
        # Método para agregar un cliente al arreglo en memoria y luego guardar todo a disco.
        
    def delete(self, client):
        self.service.remove(client)
        self.save()
        #Método para eliminar un cliente de la lista y persistir el cambio en disco.
        
    def show(self):
        for product in self.service:
             print(product) 
             # Muestra en pantalla todos los clientes guardados  cuando se llame 
             
    def update(self, cliente_obj, nuevos_datos):
        for key, value in nuevos_datos.items():
            setattr(cliente_obj, key, value)
        self.save()
        #Permite actualizar atributos de un cliente con un diccionario nuevos_datos
        # setattr(cliente_obj, key, value) 
        # cambia dinámicamente el atributo
        # finalmente vuelve a guardar.
             
    def save(self):
        with open(self.file_path, "wb") as f:
            pickle.dump(self.service, f)
            #Abre el archivo binario en modo escritura (wb) y guarda toda la lista service con pickle
            
    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                return pickle.load(f)
        else:
            return []
        #i existe el archivo, lo carga con pickle, devolviendo la lista de clientes.
        # Si no existe, devuelve una lista vacía.
        
    
    
class BillDao:
    #Clase de la factura, funciona igual que el de class ClientDao, pero ahora para factura
    def __init__(self):
        self.file_path = "facturas.bin"
        self.state = self.load()
        
    def add(self, bill):
        self.state.append(bill)
        self.save()
        
    def delete(self, bill):
        self.state.remove(bill)
        self.save()
        
    def show(self):
        for product in self.state:
             print(product) 
             
    def save(self):
        with open(self.file_path, "wb") as f:
            pickle.dump(self.state, f)
            
    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                return pickle.load(f)
        else:
            return []