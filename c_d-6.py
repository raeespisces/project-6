class Logger:
    def __init__(self):
        print ("The object has been created...")
    
    def __del__(self):
        print("The object has been destroyed")
if __name__ == "__main__":

    log = Logger()

    del log
    
