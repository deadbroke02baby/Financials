import pandas as pd

my_spending = [18500, 166500, 127900, 139000, 19000, 755000, 21253, 104100, 51500, 57900, 303499, 0]
my_earnings = [0, 41650, 754260, 0, 0, 2976201, 0, 0, 0, 4000, 22000, 66000]
categories = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]

df = pd.DataFrame({
        "category": categories,
        "spending": my_spending,
        "earnings": my_earnings
})

df["net"] = df["earnings"] - df["spending"]

print("\ntotal net:", df["net"]. sum(), "won")
df["status"] = df["net"].apply(lambda x: "surplus if x >= 0 eelse deficit")
print(df)