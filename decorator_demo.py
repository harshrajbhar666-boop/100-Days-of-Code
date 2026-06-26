def my_decorator(func):
    def wrapper():
        print("***************************")
        print("Hello! Execution Starting...")
        print("***************************")
        
        func() 
        
        print("***************************")
        print("Execution Finished! Thank You.")
        print("***************************")
        
    return wrapper  

@my_decorator
def greet():
    print("Welcome to Python Advanced Class!")

if __name__ == "__main__":
    greet()
