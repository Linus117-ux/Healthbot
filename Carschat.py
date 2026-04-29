import pandas as pd

# Load dataset with correct encoding
df = pd.read_csv("Carschat.csv", encoding="cp1252")

# Clean column names (remove spaces issues)
df.columns = df.columns.str.strip()

# Convert to lowercase for easier matching
df["Cars Names"] = df["Cars Names"].str.lower()
df["Company Names"] = df["Company Names"].str.lower()

print("🚗 CarBot: Hello! Ask me about cars (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("CarBot: Goodbye 👋")
        break

    # Find car by name
    found = df[df["Cars Names"].str.contains(user_input)]

    # Find by company
    if found.empty:
        found = df[df["Company Names"].str.contains(user_input)]

    if not found.empty:
        for _, row in found.iterrows():
            print("\n🚘 Car Found:")
            print(f"Company: {row['Company Names'].title()}")
            print(f"Car: {row['Cars Names'].title()}")
            print(f"Engine: {row['Engines']}")
            print(f"Power: {row['HorsePower']}")
            print(f"Top Speed: {row['Total Speed']}")
            print(f"0-100 km/h: {row['Performance(0 - 100 )KM/H']}")
            print(f"Price: {row['Cars Prices']}")
            print(f"Fuel: {row['Fuel Types']}")
            print(f"Seats: {row['Seats']}")
            print(f"Torque: {row['Torque']}")
            print("-" * 40)
    else:
        print("CarBot: Sorry, I couldn't find that car or company.")