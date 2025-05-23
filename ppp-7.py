class Employees:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

if __name__ == "__main__":
   
    empl= Employees("Muhammad Raees", 50000, 123-45-669)
    print(empl.name)
    print(empl._salary)
    try:
        print(empl.__ssn)
    except AttributeError:
        print("Cannot access private variable __ssn.")

        
    