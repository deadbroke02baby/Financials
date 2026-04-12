my_spending = [18500, 166500, 127900, 139000, 19000, 755000, 21253, 104100, 51500, 57900, 303499, 0]
categories = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
my_earnings = [0, 41650, 754260, 0, 0, 2976201, 0, 0, 0, 4000, 22000, 66000]
categories = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
              
total = 0

for i in range(len(my_spending)):
    total = total - my_spending[i] + my_earnings[i]
    if my_spending[i] < my_earnings[i]:
        print(categories[i], "-", - my_spending[i] + my_earnings[i], "won - too much in the bank account")
    else:
        print(categories[i], "-", - my_spending[i] + my_earnings[i], "won - meh, good enough")
print("total left:", total, "won")