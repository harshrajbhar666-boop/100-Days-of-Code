class Vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    
    def display_base_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.name}")


class ElectricCar(Vehicle):
     lega
    def __init__(self, brand, name, max_speed, battery_kwh):
        
        super().__init__(name, brand)
        
        
        self.max_speed = max_speed
        self.battery_kwh = battery_kwh

   
    def display_ev_details(self):
        self.display_base_info()  
        print(f"Max Speed    : {self.max_speed} km/h")
        print(f"Battery Cap. : {self.battery_kwh} kWh")
        print("-" * 30)



if __name__ == "__main__":
    print("--- EV Showroom Database ---\n")

    
    car1 = ElectricCar("Tesla", "Model 3", 250, 75)
    
    
    car2 = ElectricCar("Tata", "Nexon EV Max", 140, 40.5)
    
    
    car3 = ElectricCar("BYD", "Seal", 180, 82.5)

    
    car1.display_ev_details()
    car2.display_ev_details()
    car3.display_ev_details()