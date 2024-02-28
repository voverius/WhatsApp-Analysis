
import pandas as pd


def analyze_chat(df, top=5):

    """
    :param df:          DataFrame   Containing the chat records
    :param top:         Int         Number of top records to return

    :return:            Dict        Containing the results of the analysis

    -----------------------------------------------------------------------------------------------
    Description:        This function analyzes the chat records and returns the results.
    """

    results = {}

    # Format the data
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['date'] = df['date_time'].dt.date
    df['hour'] = df['date_time'].dt.hour
    df['weekday'] = df['date_time'].dt.weekday
    df['week'] = df['date_time'].dt.isocalendar().week

    #  Overall
    name = 'Overall'
    results[name] = df['user'].value_counts()

    # Busiest Day
    name = 'Busiest Day'
    results[name] = df.groupby(['user', 'date']).size().groupby(level=0).max().nlargest(top)

    # Busiest Week
    name = 'Busiest Week'
    results[name] = df.groupby(['user', 'week']).size().groupby(level=0).max().nlargest(top)

    # Fastest Back-to-Back
    name = 'Fastest Back-to-Back (minutes)'
    df_sorted = df.sort_values(by=['user', 'date_time'])
    df_sorted['diff'] = df_sorted.groupby('user')['date_time'].diff().dt.total_seconds().div(60)
    results[name] = df_sorted[df_sorted['diff'] >= 5].groupby('user')['diff'].min().nsmallest(top)

    # Stable Schedule
    name = 'Schedule Stability (hourly deviation)'
    results[name] = df.groupby('user')['hour'].std().nsmallest(top)

    # During working hours
    name = 'During Working Hours'
    df['is_working_hour'] = df.apply(lambda x: 9 <= x['hour'] <= 17 and x['weekday'] < 5, axis=1)
    results[name] = df[df['is_working_hour']].groupby('user').size().nlargest(top)

    # Working hours proportion
    name = 'Proportion During Working Hours'
    total_messages = df.groupby('user').size()
    working_hour_messages = df[df['is_working_hour']].groupby('user').size()
    results[name] = (working_hour_messages / total_messages).nlargest(top)

    # Longest Dry-Spell
    name = 'Longest Dry-Spell (days)'
    df_sorted = df.sort_values(by=['user', 'date_time']).reset_index(drop=True)
    df_sorted['diff'] = (df_sorted.groupby('user')['date_time'].diff().dt.total_seconds().
                         div(3600 * 24))
    df_sorted['diff'] = df_sorted['diff'].where(df_sorted['diff'] > 0)
    results[name] = df_sorted.groupby('user')['diff'].max().nlargest(top)

    return results
