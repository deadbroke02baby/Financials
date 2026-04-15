my_spending = [18500, 166500, 127900, 139000, 19000, 755000, 21253, 104100, 51500, 57900, 303499, 0]
my_earnings = [0, 41650, 754260, 0, 0, 2976201, 0, 0, 0, 4000, 22000, 66000]
categories = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
              
total = 0

def calculate_budget(spending, earnings, categories):
    total = 0
    for i in range(len(spending)):
        net = my_earnings[i] - my_spending[i]
        total = total + net
        if net >= 0:
            print(categories[i], "-", net, "won - surplus")
    else:
            print(categories[i], "-", net, "won - deficit")
    print("total net:", total, "won")

calculate_budget(my_spending, my_earnings, categories) #this line - same indent as 'for', not inside it