class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def total_count(cls):
        print(f"Total Object Created:{cls.count}")

if __name__ =="__main__":

    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    Counter.total_count()

        
        