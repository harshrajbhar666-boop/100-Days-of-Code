def dynamic_expense_tracker():
    print("====================================")
    print("     💰 SMART EXPENSE ANALYTICS     ")
    print("====================================\n")
    
    # Default categories ke sath dictionary
    expenses = {"Food": 0.0, "Travel": 0.0, "Bills": 0.0, "Others": 0.0}
    
    while True:
        
        available_cats = ", ".join(expenses.keys())
        print(f"Categories: {available_cats}")
        
        cat = input("Category daalein (Nayi category bhi likh sakte hain, ya 'quit' karein): ").strip().capitalize()
        
        if cat.lower() == 'quit':
            break
            
        if not cat:
            print("🚨 Category ka naam khali nahi ho sakta!\n")
            continue
            
        try:
            paisa = float(input(f"'{cat}' mein kitna kharcha hua (₹): "))
            if paisa < 0:
                print("🚨 Kharcha minus mein nahi ho sakta!\n")
                continue
                
            
            if cat not in expenses:
                expenses[cat] = paisa
                print(f"🆕 Nayi category '{cat}' jodh di gayi hai.")
            else:
                expenses[cat] += paisa  # Purane kharche mein plus kar do
                
        except ValueError:
            print("🚨 Galti! Kripya sahi amount (number) daalein.\n")
            continue
            
        print("✅ Kharcha successfully add ho gaya!\n")

    
    total_expense = sum(expenses.values())
    
    print("\n====================================")
    print("        EXPENSE REPORT SUMMARY      ")
    print("====================================")
    
    if total_expense == 0:
        print("🎉 Mubarak ho! Aaj ₹0 kharch huye.")
    else:
        print(f"{'CATEGORY':<15} | {'AMOUNT (₹)':<10} | {'PERCENTAGE':<10}")
        print("------------------------------------")
        
        
        for category, amount in expenses.items():
            percentage = (amount / total_expense) * 100
            print(f"{category:<15} | ₹{amount:<9.2f} | {percentage:.1f}%")
            
        print("------------------------------------")
        print(f"Total Money Spent : ₹{total_expense:.2f}")
    print("====================================\n")

if __name__ == "__main__":
    dynamic_expense_tracker()