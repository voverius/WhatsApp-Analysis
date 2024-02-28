
import pandas as pd
import re


def chat_read(path):

    """
    :param path:        String      Path to the chat file

    :return:            DataFrame   Containing the extracted records

    -----------------------------------------------------------------------------------------------
    Description:        This function reads the chat file and extracts the records from it. It
                        creates a DataFrame containing the date_time and user of the messages.
    """

    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}), (\d{2}:\d{2}) - (.*?): (.*)'

    records = []  # To hold processed records

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                date, time, user, message = match.groups()
                timestamp = pd.to_datetime(f'{date} {time}', dayfirst=False)

                # Count the poop emoji in the message
                emoji_count = message.count("💩")

                # Check if the message consists of only 1 or 2 poop emojis
                if emoji_count in [1, 2] and len(message.strip()) == emoji_count * len("💩"):
                    for _ in range(emoji_count):
                        records.append({'date_time': timestamp, 'user': user})

    return pd.DataFrame(records)
