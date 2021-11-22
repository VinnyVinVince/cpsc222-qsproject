import pandas as pd

file = "c211979467978047498.csv"
channel_df = pd.read_csv(file, index_col="ID")

length = []
for message in channel_df["Contents"]:
    length.append(len(message))
channel_df["Message Length"] = length

for attr in channel_df:
    print(channel_df[attr])
