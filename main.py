'''
Current Attributes:
    1. ID
    2. Timestamp
    3. Message Length
    4. Punctuation Count
'''
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def clean_data(file):
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


def graph_length(file):
    df = pd.read_csv(file + "_cleaned.csv")
    plt.figure()
    i = 1
    for length in df["Message Length"]:
        plt.bar([i], [length])
        i += 1
    plt.xlim(0, len(df) + 1)
    plt.ylim(0, 200)
    plt.show()


def graph_punct(file):
    df = pd.read_csv(file + "_cleaned.csv")
    plt.figure()
    i = 1
    for length in df["Punctuation Count"]:
        plt.bar([i], [length])
        i += 1
    plt.xlim(0, len(df) + 1)
    plt.ylim(0, 100)
    plt.show()


f_name = "messages"
clean_data(f_name)
graph_length(f_name)
#graph_punct(f_name)
