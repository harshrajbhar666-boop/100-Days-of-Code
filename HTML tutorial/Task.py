def encrypt_message(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_value = ord(char)
            shifted_value = ascii_value + shift
            encrypt_char = chr(shifted_value)
            encrypted_text += encrypt_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_message(encrypted_text, shift):
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():
            ascii_value = ord(char)
            shifted_value = ascii_value - shift
            decrypt_char = chr(shifted_value)
            decrypted_text += decrypt_char
        else:
            decrypted_text += char
    return decrypted_text
text = "DEVDOOT"
shift = 3
encrypted = encrypt_message(text, shift)
print("Encrypted:", encrypted)
decrypted = decrypt_message(encrypted, shift)
print("Decrypted:", decrypted)

#task 2

cart = [
    {"item": "sensor", "price": 1200, "qty": 2},
    {"item": "Microcontroller", "price": 2500, "qty": 1},
    {"item": "Motor", "price": 450, "qty": 4}
]

def generate_bill(cart, coupon_code):
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["qty"]
    if coupon_code == "DEVDOOT10":
        discount = subtotal * 0.10
    else:
        discount = 0
    discounted_amount = subtotal - discount
    gst = discounted_amount * 0.18
    final_amount = discounted_amount + gst

    receipt = f"""
Subtotal: ${subtotal:.2f}
Discount: ${discount:.2f}
GST (18%): ${gst:.2f}
Final Amount: ${final_amount:.2f}
"""
    return receipt

bill = generate_bill(cart, "DEVDOOT10")
print(bill)
# task 3

class MiniDaIVY:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.energy = 100
        self.battery = 100
        self.mood = "HAPPY"

    def do_task(self, task_name):
        if self.battery <= 10:
            print("System Low! Please charge Mini-DAIVY.")
            return

        self.energy -= 20
        self.battery -= 15

        print(f"{self.bot_name} completed: {task_name}")

    def charge_battery(self):
        self.battery = 100
        print("Battery charged to 100%")

    def get_status(self):
        print(f"Bot Name: {self.bot_name}")
        print(f"Energy: {self.energy}")
        print(f"Battery: {self.battery}")
        print(f"Mood: {self.mood}")

bot = MiniDaIVY("DAIVY")
bot.get_status()
bot.do_task("Scanning System")
bot.get_status()
bot.charge_battery()
bot.get_status()
    