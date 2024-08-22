
class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors
        
    def go_to(self,new_floor):
        i=0
        if new_floor>self.number_of_floors or new_floor<1:
            print('takogo etaga net')
            
        else:
            for i in range(new_floor):
                i+=1
                print(i)
            
                

    
dev=House('GK Les', 12)
print(dev.name, dev.number_of_floors)
dev2=House('Domik v derevne', 2)
print(dev2.name, dev2.number_of_floors)
dev2.go_to(2)

