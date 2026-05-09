# TASK 3 : DATA VISUALIZATION
'''
TASK 3: Data Visualization
- Create attractive visuals
- Reveal hidden insights
- Build storytelling charts
- Use matplotlib & seaborn
- Create portfolio-quality graphs
'''
print(" TASK 3 : DATA VISUALIZATION")

# Figure Size
plt.figure(figsize=(8,5))
# 1 Scatter Plot
sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="time",
    size="size",
    data=sns.load_dataset("tips")
)
plt.title("Customer Billing vs Tips Analysis")
plt.show()
# 2 Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=sns.load_dataset("tips")
)
plt.title("Average Bills by Day & Gender")
plt.show()

# 3 Histogram
plt.figure(figsize=(8,5))
sns.histplot(
    sns.load_dataset("tips")["total_bill"],
    bins=20,
    kde=True
)
plt.title("Distribution of Total Bills")
plt.show()

# 4 Heatmap
plt.figure(figsize=(10,6))
corr = sns.load_dataset("tips").corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 5 Pie Chart
tips_df = sns.load_dataset("tips")
tips_df["day"].value_counts().plot.pie(
    autopct="%1.1f%%",
    shadow=True
)
plt.title("Restaurant Orders by Day")
plt.ylabel("")
plt.show()
