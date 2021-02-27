import pandas as pd 


df = pd.read_csv("data.csv", encoding ='utf-8-sig')
gk = df.groupby("?؟")

for (index, group) in gk:
    df = pd.DataFrame(group)
    df.to_csv(index + '.group.csv', encoding ='utf-8-sig')
