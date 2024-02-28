
from app.chat_read import *
from app.chat_bodge import *
from app.chat_analyze import *
from app.results_format import *


def main(path, top=5):

    """
    :param path:        String      Path to the chat file
    :param top:         Int         Number of top records to return

    :return:            None

    -----------------------------------------------------------------------------------------------
    Description:        This function reads the chat file, analyzes the chat records, and prints
                        the results.
    """

    df = chat_read(path=path)
    df = chat_bodge(df=df)

    results = analyze_chat(df=df, top=top)

    print('\n\n')
    print(results_format(results=results))
    return


if __name__ == "__main__":
    main(path='WhatsApp Chat.txt', top=5)
