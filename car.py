class Car(object) :
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.model = model
        self.speed_limit = speed_limit
        self.company = company

    def start(self):
        print("started")    
    def stop(self):
        print("stopped")  
    def accelerate(self):
        print("accelerating")   

audi = Car("A6","red","Audi",250)  
print(audi.start())  
print (audi.stop())
print(audi.accelerate())      
print(audi.color)