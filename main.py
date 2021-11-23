import pandas as pd

file = "messages"
channel_df = pd.read_csv(file + ".csv", index_col="ID")

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
channel_df.drop(columns=["Contents", "Attachments"], inplace=True)
channel_df.to_csv(file + "_cleaned.csv")

'''
Current Attributes:
    1. ID
    2. Timestamp
    3. Message Length
    4. Punctuation Count
'''