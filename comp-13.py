class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine method via Car

# Usage
if __name__ == "__main__":
    my_engine = Engine()
    my_car = Car(my_engine)

    print(my_car.start_car())
