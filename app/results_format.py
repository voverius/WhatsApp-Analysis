
def results_format(results):

    """
    :param results:     Dict        Containing the results of the analysis

    :return:            String      Containing the formatted results

    -----------------------------------------------------------------------------------------------
    Description:        This function formats the results of the analysis into a message.

    """

    message = ""

    for category, data in results.items():

        message += f'*{category}:*\n'
        max_name_length = max(len(str(name)) for name in data.index)

        for name, value in data.items():
            if isinstance(value, float):
                formatted_value = f"{value:.2f}"

                if "proportion" in category.lower():
                    formatted_value = f"{value * 100:.0f}%"
            else:
                formatted_value = str(value)

            message += f"{str(name).ljust(max_name_length + 2)}{formatted_value}\n"
        message += "\n"
    return message
