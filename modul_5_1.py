
class House:
    def __init__(self,name,namber_of_floors):
        self.name=name
        self.namber_of_floors=namber_of_floors
        
    def go_to(self,new_floor):
        i=0
        if new_floor>self.namber_of_floors or new_floor<1:
            print('takogo etaga net')
            exit()
        while new_floor:
            i+=1
            print(i)
            if i>=new_floor:
                exit()
                

    
dev=House('GK Les', 12)
print(dev.name, dev.namber_of_floors)
dev2=House('Domik v derevne', 2)
print(dev2.name, dev2.namber_of_floors)
dev2.go_to(2)