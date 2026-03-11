import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))


for sex in tips["sex"].unique():
    subset = tips[tips["sex"] == sex]
    axes[0, 0].scatter(subset["total_bill"], subset["tip"], label=sex)

axes[0, 0].set_title("Total Bill vs Tip")
axes[0, 0].set_xlabel("Total Bill")
axes[0, 0].set_ylabel("Tip")
axes[0, 0].legend()


sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    order=["Thur", "Fri", "Sat", "Sun"],
    ax=axes[0, 1]
)

axes[0, 1].set_title("Distributia total_bill per day")


sns.histplot(
    data=tips,
    x="tip",
    hue="time",
    kde=True,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Distributia tip")


sns.barplot(
    data=tips,
    x="day",
    y="tip",
    order=["Thur", "Fri", "Sat", "Sun"],
    errorbar="ci",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Bacsis mediu per zi")

plt.tight_layout()


plt.savefig("dashboard_tips.png")

plt.show()
