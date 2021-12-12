import pandas as pd
import numpy as np

# this method will help take the relevant data from the discord csv file
# We take the following attributes
#       1. ID
#       2. Timestamp
#       3. Message Length
#       4. Punctuation Count
#       5. Has Attachment
def clean_data(channel_df, file):
    length = []                                                         # list to keep all the len of all messages
    punct = []                                                          # list to keep all punct of all messages

    for message in channel_df["Contents"]:
        msg = str(message)                                              # current content in message
        length.append(len(msg))                                         # length of the message
        count = 0                                                       # will hold punctuation count
        if "." in msg or "!" in msg or "?" in msg:
            count += msg.count(".") + msg.count("!") + msg.count("?")
        punct.append(count)

    # set values in the data
    channel_df["Message Length"] = length                               # inserting a column for message len
    channel_df["Punctuation Count"] = punct                             # inserting a column for punct coun
    attach_ser = channel_df["Attachments"]
    attach_ser.fillna("0", inplace=True)
    attachments = []

    for entry in attach_ser:
        if entry == "0":
            attachments.append(0)
        else:
            attachments.append(1)

    channel_df["Has Attachments"] = attachments
    channel_df.drop(columns=["Contents", "Attachments"], inplace=True)

    channel_df.to_csv(file + "_cleaned.csv")                            # save the dataset to a file

# this method will help split the data:
# 1. by year
# 2. then by month for each year from 2016 to 2022 (not inclusive)
def split_data(channel_df, name):
    # aggregating the data by year
    years = list(range(2016, 2022))
    data_in_years_ser = []

    # aggregates the data by year
    for year in years:
        current_year_data = pd.DataFrame(dtype=object)
        time_year = []
        message_year = []
        attachment_year = []
        punct_year = []
        index = 0
        
        for data in channel_df["Timestamp"]:
            if str(year) + "-" in data:
                time_year.append(channel_df.loc[index]["Timestamp"])
                message_year.append(channel_df.loc[index]["Message Length"])
                punct_year.append(channel_df.loc[index]["Punctuation Count"])
                attachment_year.append(channel_df.loc[index]["Has Attachments"])
            index += 1
        
        current_year_data["Timestamp"] = time_year
        current_year_data["Message Length"] = message_year
        current_year_data["Punctuation Count"] = punct_year
        current_year_data["Has Attachment"] = attachment_year
        data_in_years_ser.append(current_year_data)
        

    # aggregate the data by month of the years
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data_columns = ["Month", "Message Count", "Punctuation Count", "Attachment Count"]
    list_data_months = []

    # aggregating by the month for each year
    for year in data_in_years_ser:
        current_year_df = pd.DataFrame(dtype=object, columns=data_columns)
        # start in January
        current_month = 0
        # do for every month
        for month in months:
            total_message_len = []
            total_punct_len = []
            total_attach_len = []
            current_message_index = 0
            
            # loop through the df day messages
            for data in year["Timestamp"]:
                
                # check if current date is within the month range
                if '-' + month +'-' in data:
                    total_message_len.append(year.loc[current_message_index]["Message Length"])
                    total_punct_len.append(year.loc[current_message_index]["Punctuation Count"])
                    total_attach_len.append(year.loc[current_message_index]["Has Attachment"])
                # increment message index
                current_message_index += 1
                
            month_total_data = {'Month': month_name[current_month], 'Message Count': sum(total_message_len), 'Punctuation Count': sum(total_punct_len), 'Attachment Count': sum(total_attach_len), 'Data Owner': name}
            current_month += 1
            current_year_df = current_year_df.append(month_total_data, ignore_index=True)
        list_data_months.append(current_year_df)
    return list_data_months