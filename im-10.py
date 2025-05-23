class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Usage
if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")
    my_dog.bark()
