import pandas as pd

file = "messages.csv"
channel_df = pd.read_csv(file, index_col="ID")

length = []
for message in channel_df["Contents"]:
    length.append(len(str(message)))
channel_df["Message Length"] = length

for attr in channel_df:
    print(channel_df[attr])

'''
Current Attributes:
    1. Timestamp
    2. Contents
    3. Attachments
    4. Message Length
    5. ID
'''