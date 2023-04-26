import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


print(*[filename.split(".")[0] for filename in  os.listdir("./opinions")], sep="\n")

product_code = 96693065 #input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")
print(opinions)

#print(type(opinions.rating))

opinions.rating = opinions.rating.map(lambda x: float(x.split("/")[0].replace(",",".")))

# podstawowe statystykii opnini

#opinions_count = opinions.opinion_id.count()
#opinions_count = len(opinions)

opinions_count = opinions.shape[0] #kilka różnych opcji 

pros_count = opinions.pros.map(bool).sum() #count()
cons_count = opinions.cons.map(bool).sum()
avg_rating = opinions.rating.mean() # opinions.stars.mean().round(2)

print(f"""Dla produktu o kodzie {product_code} 
pobrano {opinions_count} opinii.
Dla {pros_count} podano liste zalet,
a dla {cons_count} podano liste wad. 
Srednia ocena produktu wynosi {avg_rating}.""")


# histogram czestosci ocen produktu
rating = opinions.rating.value_counts().reindex(list(np.arange(0,5.5,0.5)),fill_value = 0)
print(rating)
rating.plot.bar()
#plt.show()


plt.savefig(f"./plots/{product_code}_rating.png")
plt.close()


# udział rekomendacji w opiniach 

recommendations = opinions.recommendation.value_counts(dropna=False)
recommendations.plot.pie(label="", autopct="%1.1f%%")
plt.title("Rekomendacje")
plt.savefig(f"./plots/{product_code}_recommendations.png")
plt.close()