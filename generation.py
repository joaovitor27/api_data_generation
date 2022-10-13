import fordev

from baseModel.base_model import ValidatorsCpf


def generation_people(number_people: int, sex: str, age: int, uf_code: str, formatting: bool,
                      data_only: bool) -> [] or {}:
    """
    > This function generates a list of people with the specified parameters
        The function takes in the following parameters:

    - `number_people`: The number of people to generate.
    - `sex`: The sex of the people to generate.
    - `age`: The age of the people to generate.
    - `uf_code`: The UF code of the people to generate.
    - `formatting`: Whether to format the data or not.
    - `data_only`: Whether to return only the data or not

    :param number_people: number of people to be generated
    :type number_people: int
    :param sex: 'M' or 'F'
    :type sex: str
    :param age: int
    :type age: int
    :param uf_code: The code of the state you want to generate people
    :type uf_code: str
    :param formatting: True or False
    :type formatting: bool
    :param data_only: If True, the function will return a list of dictionaries, if False, it will return a list of strings
    :type data_only: bool
    :return: A list of dictionaries
    """

    result = fordev.generators.people(number_people, sex, age, uf_code, formatting, data_only)
    return result


def validators_cpf(cpf: ValidatorsCpf):
    """
    > This function validates a CPF code

    :param cpf: ValidatorsCpf
    :type cpf: ValidatorsCpf
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_cpf(cpf.cpf_code, cpf.data_only)
    return result
