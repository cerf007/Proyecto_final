class ClientDao:
    def __init__(self):
        self.service = []
        
    def add(self, client):
        self.service.append(client)
        
    def delete(self, client):
        self.service.remove(client)
        
    def show(self):
        for product in self.service:
             print(product)  
             
    def update(self, client, new_data):
        if 'name' in new_data:
            client.name = new_data['name']
        if 'last_name' in new_data:
            client.last_name = new_data['last_name']
        if 'identification' in new_data:
            client.identification = new_data['identification']
        if 'phone_number' in new_data:
            client.phone_number = new_data['phone_number']
        if 'email' in new_data:
            client.email = new_data['email']
        if 'address' in new_data:
            client.address = new_data['address']
             
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