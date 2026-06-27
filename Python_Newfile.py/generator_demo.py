
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i 

if __name__ == "__main__":
    
    my_nums = square_generator(3)
    
    
    print(next(my_nums))  
    print(next(my_nums))  
    print(next(my_nums))  
    
    
    print("\n--- Loop se bacha hua data nikalna ---")
    for num in square_generator(5):
        print(num)