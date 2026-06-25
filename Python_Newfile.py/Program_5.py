try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("❌ Galti: Aap kisi bhi number ko 0 se divide nahi kar sakte!")
    
except ValueError:
    print("❌ Galti: Kripya sirf numbers (1, 2, 3) hi enter karein!")


else:
    print(f"✅ Sahi jawab: {result}")
finally:
    print("🧹 Cleaning up... Program finished.")