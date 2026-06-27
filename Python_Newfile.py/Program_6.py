
import time


def my_decorator(asli_function):
    def wrapper():
        print("🔒 [Face ID Check]: Scanning face... Access Granted!")
        asli_function()
        print("📱 [Phone Status]: Phone Auto-Locked.\n")
    return wrapper


@my_decorator
def open_instagram():
    print("📸 Instagram open ho gaya... Reels dekh rahe hain!")

@my_decorator
def send_message():
    print("💬 Bhai ko WhatsApp message bhej diya!")


if __name__ == "__main__":
    print("--- Starting Phone Operations ---\n")
    open_instagram()  
    send_message()    
   

