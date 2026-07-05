 def calculate_bank_emi():
    print("=" * 50)
    print("SMART LOAN & EMI CALCULATOR")
    print("=" * 50)

    try:
        p = float(input("Loan Amount(Principal): "))
        r = float(input("Yearly Interest Rate(%): "))
        n = int(input("Kitne Mahine Ke Liya (Tenure in months): "))

        monthly_r = r / (12 * 100)
        
        
        numerator = p * monthly_r * ((1 + monthly_r) ** n)
        denominator = ((1 + monthly_r) ** n) - 1
        
        emi = numerator / denominator

        total_payable = emi * n
        total_interest = total_payable - p

        print("\n====================")
        print("LOAN SUMMARY REPORT")
        print("====================")

        print(f"Monthly EMI      : ₹{emi:.2f}")
        print(f"Principal Amount : ₹{p:.2f}")
        print(f"Total Interest   : ₹{total_interest:.2f}")
        print("====================")

    except ZeroDivisionError:
        print("🚨 Error: Interest rate ya months 0 nahi ho sakte!")
    except ValueError:
        print("🚨 Error: Kripya sahi numbers hi type karein!")


if __name__ == "__main__":
    calculate_bank_emi()