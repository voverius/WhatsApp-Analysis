
def chat_bodge(df):

    """
    :param df:          DataFrame      Containing the chat records

    :return:            DataFrame      Containing the bodged chat records

    -----------------------------------------------------------------------------------------------
    Description:       This function renames or removes users from the chat.

    """
    df = df[df['user'] != "Raúl Coroban"]
    df.loc[:, 'user'] = df['user'].replace("+31 6 31112622", "Koen")
    df.loc[:, 'user'] = df['user'].replace("+31 6 15507160", "Veda")
    df.loc[:, 'user'] = df['user'].replace("Julija Pienburnytė", "Julija")
    df.loc[:, 'user'] = df['user'].replace("Matteo Pallotta", "Matteo")
    df.loc[:, 'user'] = df['user'].replace("Pele Jonasse", "Pelle")
    df.loc[:, 'user'] = df['user'].replace("Kernius Malys", "Kernius")
    df.loc[:, 'user'] = df['user'].replace("Miguel Betancourt", "Miguel")
    return df
