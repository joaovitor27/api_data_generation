from fordev.generators import people


def generation_people(number_people: int, sex: str, age: int, uf_code: str, formatting: bool, data_only: bool) -> {}:
    """
    `Generate a list of people with the specified parameters.`

    The function takes in the following parameters:

    - `number_people`: The number of people to generate.
    - `sex`: The sex of the people to generate.
    - `age`: The age of the people to generate.
    - `uf_code`: The UF code of the people to generate.
    - `formatting`: Whether to format the data or not.
    - `data_only`: Whether to return only the data or not

    :param number_people: The number of people you want to generate
    :type number_people: int
    :param sex: 'M' for male, 'F' for female, 'A' for both
    :type sex: str
    :param age: The age of the person
    :type age: int
    :param uf_code: The code of the state you want to generate people from
    :type uf_code: str
    :param formatting: If True, the data will be formatted
    :type formatting: bool
    :param data_only: If True, returns only the data, without the formatting
    :type data_only: bool
    :return: A dictionary with the following keys:
        - 'people'
        - 'sex'
        - 'age'
        - 'uf_code'
        - 'formatting'
        - 'data_only'
        - 'number_people'
        - 'result'
    """
    result = people(number_people, sex, age, uf_code, formatting, data_only)
    return result
