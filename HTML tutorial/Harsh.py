'''inventory_list = [
    {"name": "3D Environment Pack", "price": 1500, "stock": 20},
    {"name": "Physics Engine Pro", "price": 5000, "stock": 5},
    {"name": "Lighting Asset Bundle", "price": 800, "stock": 50}
]

def calculate_total_inventory_value(inventory_list):
    total_value = 0
    for product in inventory_list:
        item_total = product["price"] * product["stock"]
        total_value = total_value + item_total
        
    return total_value 

def save_report(total_value):
    try:
        file = open("inventory_report.txt", "w")
        file.write("Total Inventory Value: "+str(total_value))
        file.close()
        print("Report successfully save!")
        
    except Exception as error:
        print("File save karte waqt error aaya:", error)

calculated_total = calculate_total_inventory_value(inventory_list)
save_report(calculated_total)'''

# task =1

'''def word_counter(word):
    list_word = word.lower() and word.split() 
    freq = {}
    for words in list_word: 
        if words in freq: 
            freq[words] = freq[words] + 1 
        else:
            freq[words] = 1 
    return freq 
word = "Python is easy and Python is powerful" 
print(word_counter(word))'''
                                    
#task=2

'''product_list=[("Laptop",50000,4.5),("Mouse",500,3.8 ),("Keybord",1500,4.2),("Moniter",12000,4.7)]
for (name,price,rating) in product_list:
    if rating>=4.0:
        print(f"Name={name},Rating={rating}")
highest_price = 0
highest_name = ""
for (name,price,rating) in product_list: 
    if price >= highest_price:
        highest_price = price
        highest_name = name
print(f"Product={highest_name},Price={highest_price}")''' 
# Task=3
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def get_average_marks(self):
        total = 0
        for mark in self.marks.values():
            total = total + mark
        average = total / len(self.marks)
        return average
    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Average Marks:", self.get_average_marks())
student1 = Student("Harsh", 22, {"Python": 85, "Maths": 90})
student1.display_details()



