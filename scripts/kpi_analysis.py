import pandas as pd


# =========================================
# Function: Load Data
# =========================================
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        exit()


# =========================================
# Function: Calculate Total Sales
# =========================================
def calculate_total_sales(df):
    total = df["Sales"].sum()
    print("📊 Total Sales:", round(total, 2))
    return total


# =========================================
# Function: Sales by Year
# =========================================
def sales_by_year(df):
    yearly_sales = df.groupby("Year")["Sales"].sum().sort_index()
    print("\n📅 Sales by Year:")
    print(yearly_sales)
    return yearly_sales


# =========================================
# Function: Sales by Region
# =========================================
def sales_by_region(df):
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    print("\n🌍 Sales by Region:")
    print(region_sales)
    return region_sales


# =========================================
# Function: Top 10 Products
# =========================================
def top_10_products(df):
    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n🏆 Top 10 Products:")
    print(top_products)
    return top_products


# =========================================
# Function: Monthly Sales Trend
# =========================================
def monthly_sales_trend(df):
    monthly_sales = (
        df.groupby(["Year", "Month"])["Sales"]
        .sum()
        .sort_index()
    )

    print("\n📈 Monthly Sales Trend:")
    print(monthly_sales)
    return monthly_sales


# =========================================
# Main Execution
# =========================================
if __name__ == "__main__":

    file_path = "data/processed/cleaned_sales_data.csv"

    df = load_data(file_path)

    calculate_total_sales(df)
    sales_by_year(df)
    sales_by_region(df)
    top_10_products(df)
    monthly_sales_trend(df)

    print("\n🎉 KPI Analysis Completed Successfully!")