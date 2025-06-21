class ClientDao:
    def __init__(self):
        self.service = []
        
    def add(self, client):
        self.service.append(client)
        
    def delete(self, client):
        self.service.remove(client)
        
    #def buscar(self, nombre):
    #    for producto in service:
    #        if producto.nombre 
            
        
    def show(self):
        for product in self.service:
             print(product)  # Ahora si imprimirá la representación de cada cliente
             
class BillDao:
    def __init__(self):
        self.state= []
        
    def add(self, bill):
        self.state.append(bill)
        
    def delete(self, bill):
        self.state.remove(bill)
        
    def show(self):
        for product in self.state:
             print(product) 