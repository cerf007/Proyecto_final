class ServiceDao:
    def __init__(self):
        self.service = []
        
    def add(self, product):
        self.service.append(product)
        
    def show(self):
        for product in self.service:
             print(product)  # Esto imprimirá la representación de cada cliente