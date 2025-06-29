import pickle
import os

class ClientDao:
    def __init__(self):
        self.file_path = "clientes.bin"
        self.service = self.load()
        
    def add(self, client):
        self.service.append(client)
        self.save()
        
    def delete(self, client):
        self.service.remove(client)
        self.save()
        
    def show(self):
        for product in self.service:
             print(product)  
             
    def update(self, cliente_obj, nuevos_datos):
        for key, value in nuevos_datos.items():
            setattr(cliente_obj, key, value)
        self.save()
             
    def save(self):
        with open(self.file_path, "wb") as f:
            pickle.dump(self.service, f)
            
    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as f:
                return pickle.load(f)
        else:
            return []
        
    
    
class BillDao:
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