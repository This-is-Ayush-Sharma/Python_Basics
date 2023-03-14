def FindAmount(name_of_currency, amount_in_INR):
    if(name_of_currency == "Euro"):
        print(amount_in_INR * 0.01417)
    elif(name_of_currency == "British Pound"):
        print(amount_in_INR * 0.0100)
    elif(name_of_currency == "Australian Dollar"):
        print(amount_in_INR * 0.02140)
    elif(name_of_currency == "Canadian Dollar"):
        print(amount_in_INR * 0.02027)
    else:
        print(-1)


amount_in_INR = float(input("Enter amount in INR:-"))
name_of_currency = input("Enter the currency name:-")

FindAmount(name_of_currency, amount_in_INR)