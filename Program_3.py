class CoffeeMachine:
    def __init__(self, model_name):
        self.model_name = model_name
        self._water_level = 100 

    def brew_coffee(self, size):
        if size == "Large" and self._water_level >= 50:
            self._water_level -= 50
            print(f"☕ {self.model_name}: Your Large Coffee is ready!")
        elif size == "Small" and self._water_level >= 30:
            self._water_level -= 30
            print(f"☕ {self.model_name}: Your Small Coffee is ready!")
        else:
            print("❌ Need to refill water!")

    def check_status(self):
        print(f"📊 Machine: {self.model_name} | Water Left: {self._water_level}%")

if __name__ == "__main__":
    machine = CoffeeMachine("Barista Pro")
    machine.check_status()
    machine.brew_coffee("Large")
    machine.check_status()
