import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:/Users/DELL/Downloads/2011-IndiaStateDistSbDist-0000 (1).xlsx")

df_population = df[df["Level"] == "STATE"].groupby("Name")[["TOT_P"]].sum().sort_values("TOT_P", ascending=True)
plt.figure(figsize=(10, 12))
sns.barplot(x="TOT_P", y=df_population.index, data=df_population, palette="Spectral")
plt.title("Total Population by State - Horizontal View")
plt.xlabel("Total Population")
plt.ylabel("State")
plt.tight_layout()
plt.show()

urban_rural = df[df["Level"] == "STATE"].groupby(["Name", "TRU"])[["TOT_P"]].sum().unstack().fillna(0)
urban_rural.columns = ['Rural', 'Total', 'Urban']
urban_rural["Urbanization Rate (%)"] = (urban_rural["Urban"] / urban_rural["Total"]) * 100
top_urbanized = urban_rural.sort_values("Urbanization Rate (%)", ascending=False).head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_urbanized["Urban"], labels=top_urbanized.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Urban Population Share - Top 5 Urbanized States")
plt.show()

df_lit = df[df["Level"] == "STATE"].groupby("Name")[["P_LIT", "TOT_P"]].sum()
df_lit["Literacy Rate (%)"] = (df_lit["P_LIT"] / df_lit["TOT_P"]) * 100
df_lit_sorted = df_lit.sort_values("Literacy Rate (%)")
plt.figure(figsize=(10, 12))
sns.stripplot(x="Literacy Rate (%)", y=df_lit_sorted.index, data=df_lit_sorted, color="darkgreen", size=8)
plt.title("State-wise Literacy Rate - Dot Plot")
plt.tight_layout()
plt.show()

df_gender = df[df["Level"] == "STATE"].groupby("Name")[["TOT_M", "TOT_F"]].sum()
df_gender["Gender Ratio"] = (df_gender["TOT_F"] / df_gender["TOT_M"]) * 1000
df_gender_sorted = df_gender.sort_values("Gender Ratio", ascending=True)
plt.figure(figsize=(12, 8))
plt.hlines(y=df_gender_sorted.index, xmin=900, xmax=df_gender_sorted["Gender Ratio"], color='gray')
plt.plot(df_gender_sorted["Gender Ratio"], df_gender_sorted.index, "o", markersize=8, color="crimson")
plt.title("Gender Ratio by State - Lollipop Chart")
plt.xlabel("Females per 1000 Males")
plt.tight_layout()
plt.show()

area_dict = {
    'JAMMU & KASHMIR': 222236, 'HIMACHAL PRADESH': 55673, 'PUNJAB': 50362,
    'CHANDIGARH': 114, 'UTTARAKHAND': 53483, 'HARYANA': 44212,
    'NCT OF DELHI': 1483, 'RAJASTHAN': 342239, 'UTTAR PRADESH': 243286,
    'BIHAR': 94163, 'SIKKIM': 7096, 'ARUNACHAL PRADESH': 83743,
    'NAGALAND': 16579, 'MANIPUR': 22327, 'MIZORAM': 21081, 'TRIPURA': 10486,
    'MEGHALAYA': 22429, 'ASSAM': 78438, 'WEST BENGAL': 88752,
    'JHARKHAND': 79714, 'ODISHA': 155707, 'CHHATTISGARH': 135191,
    'MADHYA PRADESH': 308350, 'GUJARAT': 196024, 'DAMAN & DIU': 112,
    'DADRA & NAGAR HAVELI': 491, 'MAHARASHTRA': 307713, 'ANDHRA PRADESH': 275045,
    'KARNATAKA': 191791, 'GOA': 3702, 'LAKSHADWEEP': 32, 'KERALA': 38852,
    'TAMIL NADU': 130058, 'PUDUCHERRY': 479, 'ANDAMAN & NICOBAR ISLANDS': 8249
}
df_density = df[df["Level"] == "STATE"].groupby("Name")[["TOT_P"]].sum().reset_index()
df_density["Area"] = df_density["Name"].map(area_dict)
df_density["Density"] = df_density["TOT_P"] / df_density["Area"]
plt.figure(figsize=(10, 6))
sns.violinplot(y="Density", data=df_density, inner="point", palette="Set3")
plt.title("Population Density Distribution - Violin Plot")
plt.tight_layout()
plt.show()

