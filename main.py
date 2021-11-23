import pandas as pd

file = "messages.csv"
channel_df = pd.read_csv(file, index_col="ID")

length = []
punct = []
for message in channel_df["Contents"]:
    msg = str(message)
    length.append(len(msg))
    count = 0
    if "." in msg or "!" in msg or "?" in msg:
        count += msg.count(".") + msg.count("!") + msg.count("?")
    punct.append(count)
channel_df["Message Length"] = length
channel_df["Punctuation Count"] = punct

for attr in channel_df:
    print(channel_df[attr])

'''
Current Attributes:
    1. ID
    2. Timestamp
    3. Contents
    4. Attachments
    5. Message Length
    6. Punctuation Count
'''