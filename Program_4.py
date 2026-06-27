class Watch:
    def __init__(self, brand):
        self.brand = brand

    def show_time(self):
        print(f"⌚ {self.brand} is showing standard time.")

class SmartWatch(Watch):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        self.steps = 0

    def walk(self, steps_walked):
        self.steps += steps_walked
        print(f"🏃 Walked {steps_walked} steps.")

    def show_fitness_report(self):
        print(f"--- {self.brand} {self.model} Report ---")
        print(f"Total Steps Today: {self.steps}")
        print("-" * 30)

if __name__ == "__main__":
    my_watch = SmartWatch("Apple", "Series 9")
    my_watch.show_time()
    my_watch.walk(4500)
    my_watch.show_fitness_report()
