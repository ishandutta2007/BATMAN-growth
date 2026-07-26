import matplotlib.pyplot as plt
import pandas as pd

# 1. Establish the historical headcount dataset
data = {
    "Company": ["Broadcom", "AMD", "Tesla", "Micron", "ASML", "Nvidia"],
    "2019": [19000, 11400, 48016, 37000, 24900, 13775],
    "2020": [20000, 12600, 70757, 40000, 28000, 18975],
    "2021": [20000, 15500, 99290, 43000, 31500, 22473],
    "2022": [20000, 25000, 127855, 48000, 39000, 26196],
    "2023": [20000, 26000, 140473, 43000, 42416, 29600],
    "2024": [20000, 26000, 140473, 43000, 42416, 29600],
    "2025": [20000, 26000, 140473, 43000, 42416, 29600],
}
engineer_pct = {
    "Broadcom": 60,
    "AMD": 70,
    "Tesla": 20,
    "Micron": 50,
    "ASML": 60,
    "Nvidia": 75,
}

df = pd.DataFrame(data)
years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]

# Apply engineer percentage to the data
for company in df["Company"]:
    if company in engineer_pct:
        df.loc[df["Company"] == company, years] = df.loc[df["Company"] == company, years] * (engineer_pct[company] / 100.0)

# Convert back to integers
df[years] = df[years].astype(int)

# 2. Configure the plot canvas
plt.figure(figsize=(11, 6))
colors = {
    "Broadcom": "#CC092F",
    "AMD": "#ED1C24",
    "Tesla": "#E31937",
    "Micron": "#0055A5",
    "ASML": "#001A72",
    "Nvidia": "#76B900",
}

# 3. Plot a trendline for each company
n_years = len(years) - 1
for idx, row in df.iterrows():
    company = row["Company"]
    counts = [row[y] for y in years]
    
    # Calculate CAGR
    start_value = counts[0]
    end_value = counts[-1]
    if start_value == 0:
        start_value = 1
    cagr = ((end_value / start_value) ** (1 / n_years)) - 1
    label_with_cagr = f"{company} (CAGR: {cagr*100:.1f}%)"
    
    plt.plot(
        years,
        counts,
        marker="o",
        linewidth=2.5,
        color=colors[company],
        label=label_with_cagr,
    )
    
    # Annotate each point for the company
    for i, count in enumerate(counts):
        plt.annotate(f"{count:,}", (years[i], count), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=8, color=colors[company])

# Calculate and plot the total of all companies for each year
totals = df[years].sum()
plt.plot(
    years, 
    totals, 
    marker="D", 
    linewidth=3, 
    color="black", 
    linestyle="--",
    label="Total (All Companies)"
)
for i, total_val in enumerate(totals):
    plt.annotate(f"{total_val:,}", (years[i], total_val), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=9, fontweight='bold')

# 4. Formatter enhancements for readability
plt.title("BATMAN Historical Engineer Headcount Trends (2019 - 2025)", fontsize=14, pad=15)
plt.xlabel("Fiscal Year", fontsize=11, labelpad=10)
plt.ylabel("Total Global Engineers", fontsize=11, labelpad=10)

# Formats large numbers on the Y-axis with commas (e.g., 1,500,000)
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, p: format(int(x), ","))
)

# Optional: Uncomment the next line if you want to inspect growth curves clearly without Amazon skewing the axis
plt.yscale('log')

plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(title="Companies", frameon=True, facecolor="white")
plt.tight_layout()

# 5. Display the graph
plt.savefig("assets/BATMAN_growth.png")

# 6. Calculate and plot year-over-year growth
plt.figure(figsize=(11, 6))
df_growth = df.set_index('Company')[years].diff(axis=1).dropna(axis=1)

# Plotting using pandas wrapper around matplotlib
df_growth.T.plot(kind='bar', figsize=(11, 6), color=[colors[c] for c in df_growth.index], width=0.7, ax=plt.gca())

plt.title("BATMAN Year-over-Year Engineer Growth (2020 - 2025)", fontsize=14, pad=15)
plt.xlabel("Fiscal Year", fontsize=11, labelpad=10)
plt.ylabel("Net Engineer Change", fontsize=11, labelpad=10)
plt.xticks(rotation=0)

# Formats numbers with commas
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, p: format(int(x), ","))
)

plt.grid(True, linestyle="--", alpha=0.5, axis='y')
plt.legend(title="Companies", frameon=True, facecolor="white")
plt.tight_layout()
plt.savefig("assets/BATMAN_yoy_growth.png")

plt.show()
