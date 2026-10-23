'''class BaseUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"

class AdminUser(BaseUser):
    def __init__(self, username, email, permissions_level):
        self.permissions_level = permissions_level
        super().__init__(username, email)
        
    def get_profile(self):
        return f"ADMIN: {self.username} | Email: {self.email} | Permissions: {self.permissions_level}"

normal_user = BaseUser("Rohan", "rohan@email.com")
admin_user = AdminUser("Harsh", "harshrajbhar666@gmail.com", "SuperAdmin")

print(normal_user.get_profile())
print(admin_user.get_profile())'''



# programm :Model3D

'''class Model3D:
    def __init__(self,name,color):
        self.name=name
        self.color=color

        def  get_profile(self):
            return "Rendering Model: {name} | Color: {color}"

            class method(Model3D):
                def __init__(self,name,color,animation_type):
                    self.animation_type=animation_type
                    super.__init__(name,color)

                def get_profile(self):
                    return "Rendering Animated Model: {name} | Color: {color} | Animation: {animation_type}"
                
                    

                user_modal=Modal3D("harsh","yello")
                user_method=method("bablu","Black","3D_animation")

                print(user_modal.get_profile())
                print(user_method.get_profile())'''# Harsh.css'''


#"Devdoots Assignment 03 - Python OOPs Encapsulation & Abstraction            
'''class SecureBankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 5000  # Private balance
        self.__pin = 1234      # Private pin 

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin and amount <= self.__balance:
            self.__balance = self.__balance - amount
            return "Withdrawal successful!"
        else:
            return "Invalid PIN or Insufficient Balance"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin and 1000 <= new_pin <= 9999:
            self.__pin = new_pin
            return "PIN successfully changed!"
        else:
            return "Invalid old PIN or new PIN must be 4 digits"

my_account = SecureBankAccount("Harsh User") 
print(my_account.change_pin(1234, 9999))
print(my_account.withdraw(1111, 1000))

# Task 2: Al Model Pipeline Blueprint (Abstraction Practice)
from abc import ABC, abstractmethod

class BaseAIModel(ABC):
    @abstractmethod
    def train_model(self, dataset_name):
        pass

    @abstractmethod
    def evaluate_accuracy(self):
        pass

class VisionModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training Vision Model on {dataset_name} image dataset..."

class NLPModel(BaseAIModel):
    def train_model(self, dataset_name):
        return f"Training NLP Model on {dataset_name} text dataset..."

        def evaluate_accuracy(self):
           return "NLP Model Sentiment Classification Accuracy: 88%"'''




#Task 1: Safe Division Utility ka Blueprint

def self_calculator(num1,num2):
    try:
        ans=num1/num2

    except ZeroDivisionError:
        return "Error: Zero se divide nahi kar sakte"

    except TypeError:
        return "Error: Dono inputs numbers (int/float) hone chahiye!"
print(self_calculator(25,5))
print(self_calculator(645345,0))
print(self_calculator(44,"A"))

#Task 2: Devdoots Activity Logger (File I/O)    

def team_activity_logger():
    file_name = "Devdoots_activity.txt"
    
    with open(file_name, "a") as file:
        file.write("[Harsh]: Practiced Exception Handling File I/O\n")
        
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(content)        
            
    except FileNotFoundError:     
        print("Error: File nahi mili!")

team_activity_logger()


