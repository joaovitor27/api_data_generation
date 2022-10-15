import fordev

from baseModel.base_model import (ValidatorsCpf, ValidatorsRg, ValidatorsBankAccount, ValidatorsCertificate,
                                  ValidatorsCNH, ValidatorsCNPJ, ValidatorsCreditCard, ValidatorsPisPasep,
                                  ValidatorsRenavam, ValidatorsVoterTitle, ValidatorsStateRegistration)


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
    :param data_only: If True, the function will return a list of dictionaries, if False, it will return a list of
    strings
    :type data_only: bool
    :return: A list of dictionaries
    """

    result = fordev.generators.people(number_people, sex, age, uf_code, formatting, data_only)
    return result


def generation_cpf(uf_code: str, formatting: bool, data_only: bool):
    """
    `generation_cpf(uf_code: str, formatting: bool, data_only: bool)`

    This function generates a CPF number

    :param uf_code: The state code of the CPF
    :type uf_code: str
    :param formatting: True or False
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without formatting
    :type data_only: bool
    :return: A CPF number.
    """
    result = fordev.generators.cpf(uf_code, formatting, data_only)
    return result


def generation_city(uf_code: str, data_only: bool):
    """
    `Generate a city name for a given state code.`

    The first line of the function is a docstring. It's a string that describes what the function does. It's a good
    practice to write docstrings for all your functions

    :param uf_code: The state code, for example: SP, RJ, MG, etc
    :type uf_code: str
    :param data_only: If True, the function will return only the data, without the header
    :type data_only: bool
    :return: A list of dictionaries with the following keys:
        - uf_code
        - city_name
        - city_code
        - city_population
        - city_area
        - city_density
        - city_latitude
        - city_longitude
        - city_elevation
        - city_timezone
        - city
    """
    result = fordev.generators.city(uf_code, data_only)
    return result


def generation_rg(formatting: bool, data_only: bool):
    """
    `generation_rg` generates a random number

    :param formatting: bool
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without the formatting
    :type data_only: bool
    :return: A random RG number.
    """
    result = fordev.generators.rg(formatting, data_only)
    return result


def generation_bank_account(bank: int, uf_code: str, data_only: bool):
    """
    `generation_bank_account(bank: int, uf_code: str, data_only: bool)`

    This function returns a bank account number

    :param bank: The bank's code
    :type bank: int
    :param uf_code: The state code, for example, SP, RJ, MG, etc
    :type uf_code: str
    :param data_only: If True, the function will return only the data, without the bank account format
    :type data_only: bool
    :return: A bank account number.
    """
    result = fordev.generators.bank_account(bank, uf_code, data_only)
    return result


def generation_certificate(type_: str, formatting: bool, data_only: bool):
    """
    Generate a certificate

    :param type_: The type of certificate you want to generate
    :type type_: str
    :param formatting: True/False
    :type formatting: bool
    :param data_only: If True, the function will return the data only, without the formatting
    :type data_only: bool
    :return: A dictionary with the following keys:
        - 'certificate_type'
        - 'certificate_number'
        - 'certificate_date'
        - 'certificate_expiration_date'
        - 'certificate_issuer'
        - 'certificate_issuer_address'
        - 'certificate_issuer_phone'
    """
    result = fordev.generators.certificate(type_, formatting, data_only)
    return result


def generation_cnh(data_only: bool):
    """
    `generation_cnh` generates a random CNH

    :param data_only: If True, the function will return only the data, without the mask
    :type data_only: bool
    :return: A string with the generated CNH.
    """
    result = fordev.generators.cnh(data_only)
    return result


def generation_cnpj(formatting: bool, data_only: bool):
    """
    Generate a CNPJ

    :param formatting: True or False. If True, the result will be formatted
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without formatting
    :type data_only: bool
    :return: A CNPJ number.
    """
    result = fordev.generators.cnpj(formatting, data_only)
    return result


def generation_company(uf_code: str, age: int, formatting: bool, data_only: bool):
    """
    `Generate a company name and CNPJ.`

    The first line of the function is a docstring. It's a string that describes what the function does. It's optional,
    but it's good practice to include one

    :param uf_code: The state code of the company
    :type uf_code: str
    :param age: The age of the company
    :type age: int
    :param formatting: If True, the result will be formatted
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without formatting
    :type data_only: bool
    :return: A dictionary with the following keys:
        - cnpj
        - name
        - fantasy_name
        - state_registration
        - municipal_registration
        - address
        - neighborhood
        - city
        - state
        - zip_code
        - phone
        - email
        - website
        - foundation_date
        -
    """
    result = fordev.generators.company(uf_code, age, formatting, data_only)
    return result


def generation_credit_card(bank: int, formatting: bool, data_only: bool):
    """
    Generate a credit card number

    :param bank: int - the bank number, if you want to generate a card from a specific bank
    :type bank: int
    :param formatting: True/False
    :type formatting: bool
    :param data_only: If True, the function will return only the data of the credit card, without formatting
    :type data_only: bool
    :return: A credit card number.
    """
    result = fordev.generators.credit_card(bank, formatting, data_only)
    return result


def generation_pis_pasep(formatting: bool, data_only: bool):
    """
    > Generates a random PIS/PASEP number

    :param formatting: If True, the result will be formatted as a string. If False, the result will be a list
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without the formatting
    :type data_only: bool
    :return: A string with the PIS/PASEP number.
    """
    result = fordev.generators.pis_pasep(formatting, data_only)
    return result


def generation_renavam(data_only: bool):
    """
    `generation_renavam` generates a random RENAVAM

    :param data_only: If True, the function will return only the data, without the mask
    :type data_only: bool
    :return: A string with the generated renavam.
    """
    result = fordev.generators.renavam(data_only)
    return result


def generation_state_registration(uf_code: str, formatting: bool, data_only: bool):
    """
    > Generates a random state registration number for a given state

    :param uf_code: The state code, which can be found in the list below
    :type uf_code: str
    :param formatting: if True, the result will be formatted
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without formatting
    :type data_only: bool
    :return: A string with the state registration number.
    """
    result = fordev.generators.state_registration(uf_code, formatting, data_only)
    return result


def generation_uf(n: int, data_only):
    """
    It generates a random undirected graph with n vertices

    :param n: the number of vertices in the graph
    :type n: int
    :param data_only: if True, then the function will return only the data, without the header
    :return: A list of lists.
    """
    result = fordev.generators.uf(n, data_only)
    return result


def generation_vehicle(brand_code: int, uf_code: str, formatting: bool, data_only: bool):
    """
    `generation_vehicle(brand_code: int, uf_code: str, formatting: bool, data_only: bool)`

    This function returns a random vehicle plate number

    :param brand_code: The code of the brand of the vehicle
    :type brand_code: int
    :param uf_code: The state code of the vehicle
    :type uf_code: str
    :param formatting: If True, the result will be formatted
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without the formatting
    :type data_only: bool
    :return: A dictionary with the following keys:
        - 'brand': The brand of the vehicle
        - 'model': The model of the vehicle
        - 'year': The year of the vehicle
        - 'color': The color of the vehicle
        - 'plate': The plate of the vehicle
        - 'uf': The uf of the vehicle
        - 'data':
    """
    result = fordev.generators.vehicle(brand_code, uf_code, formatting, data_only)
    return result


def generation_voter_title(uf_code: str, data_only: bool):
    """
    It generates a voter title for a given state

    :param uf_code: The two-letter code for the state
    :type uf_code: str
    :param data_only: if True, the function will return only the data, without the title
    :type data_only: bool
    :return: A dictionary with the following keys:
        - 'voter_title_number'
        - 'voter_title_state'
        - 'voter_title_uf'
        - 'voter_title_uf_code'
        - 'voter_title_uf_code_int'
        - 'voter_title_uf_code
    """
    result = fordev.generators.voter_title(uf_code, data_only)
    return result


def generation_vehicle_brand(n: int, data_only: bool):
    """
    Generate a list of vehicle brands

    :param n: int - number of records to generate
    :type n: int
    :param data_only: If True, the generator will return only the data, not the data and the label
    :type data_only: bool
    :return: A list of vehicle brands.
    """
    result = fordev.generators.vehicle_brand(n, data_only)
    return result


def generation_vehicle_plate(uf_code: str, formatting: bool, data_only: bool):
    """
    Generates a random vehicle plate number for the given uf_code

    :param uf_code: The state code of the vehicle plate
    :type uf_code: str
    :param formatting: If True, the result will be formatted as a vehicle plate
    :type formatting: bool
    :param data_only: If True, the function will return only the data, without formatting
    :type data_only: bool
    :return: A vehicle plate number.
    """
    result = fordev.generators.vehicle_plate(uf_code, formatting, data_only)
    return result


def generation_renavam_(data_only: bool):
    """
    `generation_renavam_` generates a random renavam

    :param data_only: If True, the function will return only the data, without the mask
    :type data_only: bool
    :return: A string with the generated renavam.
    """
    result = fordev.generators.renavam(data_only)
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


def validators_rg(rg: ValidatorsRg):
    """
    > This function validates a Brazilian RG (Registro Geral) code

    :param rg: ValidatorsRg
    :type rg: ValidatorsRg
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_rg(rg.rg_code, rg.data_only)
    return result


def validators_bank_account(bank_account: ValidatorsBankAccount):
    """
    `validators_bank_account` validates a bank account

    :param bank_account: ValidatorsBankAccount
    :type bank_account: ValidatorsBankAccount
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_bank_account(bank_account.bank, bank_account.agency, bank_account.account,
                                                     bank_account.data_only)
    return result


def validators_certificate(certificate: ValidatorsCertificate):
    """
    `validators_certificate` checks if a certificate is valid

    :param certificate: ValidatorsCertificate - the certificate to be validated
    :type certificate: ValidatorsCertificate
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_certificate(certificate.certificate_code, certificate.data_only)
    return result


def validators_cnh(cnh: ValidatorsCNH):
    """
    > This function validates a Brazilian driver's license number (CNH) and returns a boolean value

    :param cnh: ValidatorsCNH
    :type cnh: ValidatorsCNH
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_cnh(cnh.cnh_code, cnh.data_only)
    return result


def validators_cnpj(cnpj: ValidatorsCNPJ):
    """
    > This function validates a CNPJ code

    :param cnpj: ValidatorsCNPJ
    :type cnpj: ValidatorsCNPJ
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_cnpj(cnpj.cnpj_code, cnpj.data_only)
    return result


def validators_credit_card(credit_card: ValidatorsCreditCard):
    """
    `validators_credit_card`: Validates a credit card number

    :param credit_card: ValidatorsCreditCard
    :type credit_card: ValidatorsCreditCard
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_credit_card(credit_card.flag, credit_card.credit_card_code,
                                                    credit_card.data_only)
    return result


def validators_pis_pasep(pis_pasep: ValidatorsPisPasep):
    """
    > This function validates a PIS/PASEP number

    :param pis_pasep: ValidatorsPisPasep
    :type pis_pasep: ValidatorsPisPasep
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_pis_pasep(pis_pasep.pis_pasep_code, pis_pasep.data_only)
    return result


def validators_renavam(renavam: ValidatorsRenavam):
    """
    > This function validates a Brazilian vehicle registration number (Renavam)

    :param renavam: ValidatorsRenavam
    :type renavam: ValidatorsRenavam
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_renavam(renavam.renavam_code, renavam.data_only)
    return result


def validators_state_registration(state_registration: ValidatorsStateRegistration):
    """
    > It validates a Brazilian state registration number

    :param state_registration: ValidatorsStateRegistration
    :type state_registration: ValidatorsStateRegistration
    :return: A boolean value.
    """
    result = fordev.validators.is_valid_state_registration(state_registration.uf_code,
                                                           state_registration.state_registration_code,
                                                           state_registration.data_only)
    return result


def validators_voter_title_code(voter_title: ValidatorsVoterTitle):
    """
    > This function validates the voter title code

    :param voter_title: ValidatorsVoterTitle
    :type voter_title: ValidatorsVoterTitle
    :return: A boolean value.
    """

    result = fordev.validators.is_valid_voter_title(voter_title.voter_title_code, voter_title.data_only)
    return result


def get_all_uf_code():
    """
    > Returns a list of all the UF codes
    :return: A list of all the UF codes.
    """
    return fordev.consts.ALL_UF_CODE


def get_all_bank_flags():
    """
    > Returns a list of all bank flags
    :return: A list of all the bank flags.
    """
    return fordev.consts.ALL_BANK_FLAGS


def get_all_bank_flags_two():
    """
    > Returns a list of all bank flags for the second bank
    :return: A list of all the bank flags.
    """
    return fordev.consts.ALL_BANK_FLAGS_2


def get_all_vehicle_brands():
    """
    > Returns a list of all vehicle brands
    :return: A list of all vehicle brands.
    """
    return fordev.consts.ALL_VEHICLE_BRANDS
