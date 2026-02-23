import pandas as pd

# =====================================
# 1️⃣ Load Raw Dataset
# =====================================
try:
    df = pd.read_csv("data/raw/train.csv")
    print("✅ Raw data loaded successfully!")
except FileNotFoundError:
    print("❌ File not found. Please check the file path.")
    exit()

# =====================================
# 2️⃣ Convert Date Columns (European Format)
# =====================================
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

# =====================================
# 3️⃣ Feature Engineering
# =====================================
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month_Name"] = df["Order Date"].dt.month_name()
df["Quarter"] = df["Order Date"].dt.quarter

# =====================================
# 4️⃣ Remove Duplicates
# =====================================
df = df.drop_duplicates()

# =====================================
# 5️⃣ Handle Missing Values
# =====================================
df = df.dropna(subset=["Postal Code"])

# =====================================
# 6️⃣ Save Cleaned Dataset
# =====================================
df.to_csv("data/processed/cleaned_sales_data.csv", index=False)

print("🎉 Data cleaned successfully and saved to data/processed/")