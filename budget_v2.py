import pandas as pd
import matplotlib.pyplot as plt

my_spending = [18500, 166500, 127900, 139000, 19000, 755000, 21253, 104100, 51500, 57900, 303499, 0]
my_earnings = [0, 41650, 754260, 0, 0, 2976201, 0, 0, 0, 4000, 22000, 66000]
categories = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]

df = pd.DataFrame({
    "category": categories,
    "spending": my_spending,
    "earnings": my_earnings
})

df["net"] = df["earnings"] - df["spending"]
df["status"] = df["net"].apply(lambda x: "surplus" if x >= 0 else "deficit")

print(df)
print("\ntotal net:", df["net"]. sum(), "won")

df.plot(kind="bar", x="category", y=["spending", "earnings"], figsize=(10,6)) 
plt.title("Montly Budget - Spending vs Earnings")
plt.xlabel("Month")
plt.ylabel("Amount (won)")
plt.tight_layout()
plt.show()

colors = ["green" if x >= 0 else "red" for x in df["net"]]
df.plot(kind="bar", x="category", y="net", color=colors, figsize=(10,6))
plt.title("Monthly Net - Surplus vs Deficit")
plt.axhline(y=0, color="black", linewidth=0.8)
plt.tight_layout()
plt.show()