class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
        self.speed = 0

    def start(self):
        self.is_running = True
        print(self.brand, self.model, "started")

    def stop(self):
        self.is_running = False
        self.speed = 0
        print(self.brand, self.model, "stopped")

    def accelerate(self, amount):
        self.speed += amount
        print(self.brand, self.model, "speed:", self.speed)

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(self.brand, self.model, "speed:", self.speed)

    def display_info(self):
        print(self.year, self.color, self.brand, self.model)


Toyota = Car("Toyota", "Corolla", 2020, "White")
Honda = Car("Honda", "Civic", 2019, "Black")
Tesla = Car("Tesla", "Model 3", 2024, "Red")

Toyota.start()
Toyota.accelerate(30)
Toyota.brake(10)
Toyota.display_info()

print()

Honda.start()
Honda.display_info()

print()

Tesla.display_info()