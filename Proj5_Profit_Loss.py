def shop_profit_loss_analytics():
    print("====================================")
    print("     DAILY PROFIT/LOSS ANALYTICS   ")
    print("====================================\n")
    
    # STEP 1: 7 Din Ka Data Jole (Lists) Mein Bharna
    sales_list = []
    expense_list = []
    
    print(" Pure hafte (7 Din) ka data entry karein:")
    for day in range(1, 8):
        while True:
            try:
                sales = float(input(f"Day {day} ki total sales (Kamai) ₹: "))
                expense = float(input(f"Day {day} ka total kharcha ₹: "))
                
                if sales < 0 or expense < 0:
                    print(" Galti! Kamai ya kharcha minus mein nahi ho sakta. Fir se daalein.")
                    continue
                    
                sales_list.append(sales)
                expense_list.append(expense)
                break  # Sahi input milne par loop se bahar aur agle din par jump
            except ValueError:
                print(" Error: Kripya sahi number type karein!\n")

    # STEP 2: Hafte Ka Total Aur Average Nikalna
    total_sales = sum(sales_list)
    total_expenses = sum(expense_list)
    
    avg_sales = total_sales / 7
    avg_expenses = total_expenses / 7
    
    net_result = total_sales - total_expenses

    # STEP 3: Final Report Display Aur Conditional Logic
    print("\n====================================")
    print("        WEEKLY BUSINESS REPORT      ")
    print("====================================")
    print(f"Total Weekly Sales    : ₹{total_sales:.2f}")
    print(f"Total Weekly Expenses : ₹{total_expenses:.2f}")
    print(f"Average Daily Sales   : ₹{avg_sales:.2f}")
    print(f"Average Daily Expense : ₹{avg_expenses:.2f}")
    print("------------------------------------")
    
    if net_result > 0:
        # Profit Percentage calculation
        profit_percent = (net_result / total_expenses) * 100
        print(f" STATUS             : PROFIT ")
        print(f"Net Munafe (Profit)   : ₹{net_result:.2f}")
        print(f"Profit Percentage     : {profit_percent:.2f}%")
    elif net_result < 0:
        # Loss Percentage calculation (Net result minus mein hoga toh use plus karke dikhane ke liye abs() ya - lagate hain)
        loss_amount = abs(net_result)
        loss_percent = (loss_amount / total_expenses) * 100
        print(f" STATUS             : LOSS ")
        print(f"Net Nuksan (Loss)     : ₹{loss_amount:.2f}")
        print(f"Loss Percentage       : {loss_percent:.2f}%")
    else:
        print(f"STATUS             : NO PROFIT, NO LOSS")
        print(f"Hisaab Barabar Raha!")
        
    print("====================================\n")

if __name__ == "__main__":
    shop_profit_loss_analytics()
