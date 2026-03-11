import pandas as pd
import seaborn as sns


tips = sns.load_dataset("tips")


print("Dimensiune dataset:", tips.shape)

print("\nTipuri de date:")
print(tips.dtypes)

print("\nStatistici descriptive:")
print(tips.describe())


tip_mediu = tips.groupby(["day", "sex"]).mean(numeric_only=True)

print("\nBacsis mediu per zi si sex:")
print(tip_mediu["tip"])


tips_copy = tips.copy()
tips_copy["procent_bacsis"] = tips_copy["tip"] / tips_copy["total_bill"] * 100

print("\nDataset cu procent_bacsis:")
print(tips_copy.head())


top5 = tips_copy.sort_values("procent_bacsis", ascending=False).head(5)

print("\nTop 5 mese cele mai generoase:")
print(top5)


mese = tips.groupby(["day", "smoker"]).size()

print("\nNumar mese per zi si smoker:")
print(mese)
