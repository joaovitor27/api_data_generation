from fastapi import FastAPI
from core import generation, validators, consts
from baseModel.base_model import (ValidatorsCpf, ValidatorsRg, ValidatorsBankAccount, ValidatorsCertificate,
                                  ValidatorsCNH, ValidatorsCNPJ, ValidatorsCreditCard, ValidatorsPisPasep,
                                  ValidatorsRenavam, ValidatorsVoterTitle, ValidatorsStateRegistration)
app = FastAPI()


def data_result(data):
    return {"result": data}


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/api/generation-people")
async def generation_people(number_people: int = 1, sex: str = 'R', age: int = 18, uf_code: str = '',
                            formatting: bool = False, data_only: bool = True) -> {}:
    """
    `Generate people data.`

    The function takes the following arguments:

    - `number_people`: The number of people to generate.
    - `sex`: The sex of the people to generate.
    - `age`: The age of the people to generate.
    - `uf_code`: The UF code of the people to generate.
    - `formatting`: Whether to format the data.
    - `data_only`: Whether to return only the data

    :param number_people: Number of people to be generated, defaults to 1
    :type number_people: int (optional)
    :param sex: 'M' for male, 'F' for female, 'R' for random, defaults to R
    :type sex: str (optional)
    :param age: The age of the person to be generated, defaults to 18
    :type age: int (optional)
    :param uf_code: The state code, for example, SP, RJ, MG, etc
    :type uf_code: str
    :param formatting: If True, the result will be formatted, defaults to False
    :type formatting: bool (optional)
    :param data_only: If True, returns only the data, if False, returns the data and the status code, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the key "result" and the value of the result of the function generation_people.
    """

    result = generation.generation_people(number_people, sex, age, uf_code, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-company")
async def generation_company(uf_code: str = 'SP', age: int = 1, formatting: bool = True, data_only: bool = True) -> {}:
    """
    `Generate a person's data.`

    The first line of the function is a docstring. This is a special string that is used to document the function. It
    is the first statement in the function

    :param uf_code: The state code, which is the state where the company is located, defaults to SP
    :type uf_code: str (optional)
    :param age: The age of the person, defaults to 1
    :type age: int (optional)
    :param formatting: If True, the data will be formatted, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, only the data will be returned, if False, the data will be returned with the formatting,
    defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the key "result" and the value of the result of the function generation_company.
    """
    result = generation.generation_company(uf_code, age, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-renavam")
async def generation_renavam(data_only: bool = True) -> {}:
    """
    It generates a random RENAVAM number.

    :param data_only: If True, the function will return only the data, if False, it will return the data and the status
    code, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - data: The data generated
        - status: The status of the request
        - message: The message of the request
    """
    result = generation.generation_renavam(data_only)
    return data_result(result)


@app.get("/api/generation-vehicle")
async def generation_vehicle(brand_color: int = 0, uf_code: str = '', formatting: bool = True,
                             data_only: bool = True) -> {}:
    """
    `Generate a vehicle data.`

    :param brand_color: int = 0, defaults to 0
    :type brand_color: int (optional)
    :param uf_code: The state code, for example: SP, RJ, MG, etc
    :type uf_code: str
    :param formatting: If True, the data will be formatted, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, only the data will be returned, if False, the data will be returned with the status code,
    defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - 'brand_color': The brand color of the vehicle.
        - 'uf_code': The UF code of the vehicle.
        - 'plate': The plate of the vehicle.
        - 'plate_format': The plate of the vehicle formatted.
        - 'plate_format_uf': The plate of the vehicle
    """
    result = generation.generation_vehicle(brand_color, uf_code, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-certificate")
async def generation_certificate(type_: str, formatting: bool = True, data_only: bool = True) -> {}:
    """
    It generates a certificate.

    :param type_: The type of certificate to be generated
    :type type_: str
    :param formatting: If True, the result will be formatted, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, the result will be returned as a dictionary, otherwise it will be returned as a JSON
    string, defaults to True
    :type data_only: bool (optional)
    :return: The result of the generation of the certificate.
    """
    result = generation.generation_certificate(type_, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-bank-account")
async def generation_bank_account(bank: int = 0, uf_code: str = '', data_only: bool = True) -> {}:
    """
    `Generate a bank account number.`

    The function has the following parameters:

    * `bank`: The bank code.
    * `uf_code`: The UF code.
    * `data_only`: If `True`, the function will return only the data

    :param bank: int = 0,, defaults to 0
    :type bank: int (optional)
    :param uf_code: The state code, for example: SP, RJ, MG, etc
    :type uf_code: str
    :param data_only: If True, the result will be a dictionary with the following structure:, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the bank account information.
    """
    result = generation.generation_bank_account(bank, uf_code, data_only)
    return data_result(result)


@app.get("/api/generation-data-city")
async def generation_data_city(uf_code: str = 'SP', data_only: bool = True) -> {}:
    """
    It returns the cities of the state of São Paulo.

    :param uf_code: str = 'SP', defaults to SP
    :type uf_code: str (optional)
    :param data_only: If True, only the data will be returned, if False, the data and the metadata will be returned,
    defaults to True
    :type data_only: bool (optional)
    :return: The generation data of the city.
    """
    result = generation.generation_data_city(uf_code, data_only)
    return data_result(result)


@app.get("/api/generation-cnh")
async def generation_cnh(data_only: bool = True) -> {}:
    """
    `Generate a valid CNH number.`

    The function `generation_cnh` has the following parameters:

    | Parameter | Tags | Description |
    |-----------|------|-------------|
    | dataOnly |

    :param data_only: If True, only the data will be returned. If False, the data and the status will be returned,
    defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - 'cnh': The generated CNH
        - 'cnh_type': The type of CNH
        - 'cnh_category': The category of CNH
        - 'cnh_expiration_date': The expiration date of the CNH
        - 'cnh_emission_date': The emission date
    """
    result = generation.generation_cnh(data_only)
    return data_result(result)


@app.get("/api/generation-cnh")
async def generation_cnpj(formatting: bool = True, data_only: bool = True) -> {}:
    """
    Generates a CNPJ number.

    :param formatting: bool = True, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, the result will be a dictionary with the following keys:, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following structure:
    {
        "data": {
            "cnpj": "string",
            "cnpj_format": "string"
        },
        "status": "string"
    }
    """
    result = generation.generation_cnpj(formatting, data_only)
    return data_result(result)


@app.get("/api/generation-pis-pasep")
async def generation_pis_pasep(formatting: bool = True, data_only: bool = True) -> {}:
    """
    Generates a PIS/PASEP number

    :param formatting: bool = True, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, the function will return only the data, without the formatting, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - 'data': A dictionary with the following keys:
            - 'pis_pasep': A string with the generated PIS/PASEP number.
            - 'pis_pasep_format': A string with the formatted PIS/PASEP number.
        - 'status': A string with the status of
    """
    result = generation.generation_pis_pasep(formatting, data_only)
    return data_result(result)


@app.get("/api/generation-uf")
async def generation_uf(uf_code_number: int = 1, data_only: bool = True) -> {}:
    """
    `Generate a random UF`

    :param uf_code_number: The code number of the state you want to generate the data for, defaults to 1
    :type uf_code_number: int (optional)
    :param data_only: If True, the result will be a dictionary with the data only. If False, the result will be a
    dictionary with the data and the metadata, defaults to True
    :type data_only: bool (optional)
    :return: The result of the generation of the uf code number.
    """
    result = generation.generation_uf(uf_code_number, data_only)
    return data_result(result)


@app.get("/api/generation-rg")
async def generation_rg(formatting: bool = True, data_only: bool = True) -> {}:
    """
    `generation_rg` returns a random generation

    :param formatting: bool = True, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, the result will be a dictionary with the following keys:, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - 'data': A list of dictionaries with the following keys:
            - 'id': The id of the generation
            - 'name': The name of the generation
            - 'main_region': The main region of the generation
            - 'version_groups': A list of dictionaries with the following keys:
                -
    """
    result = generation.generation_rg(formatting, data_only)
    return data_result(result)


@app.get("/api/generation-state-registration")
async def generation_state_registration(uf_code: str = 'SP', formatting: bool = True, data_only: bool = True) -> {}:
    """
    It returns the state registration number of the state of São Paulo.

    :param uf_code: The state code, which is the acronym of the state, defaults to SP
    :type uf_code: str (optional)
    :param formatting: If True, the data will be formatted, defaults to True
    :type formatting: bool (optional)
    :param data_only: If True, only the data will be returned. If False, the data will be returned with the metadata,
    defaults to True
    :type data_only: bool (optional)
    :return: The result of the function generation_state_registration
    """
    result = generation.generation_state_registration(uf_code, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-vehicle-brand")
async def generation_vehicle_brand(uf_code_number: int = 1, data_only: bool = True) -> {}:
    """
    `Generate a random vehicle brand.`

    The function `generation_vehicle_brand` has the following parameters:

    | Parameter | Type | Required | Default | Description |
    | --- | --- | --- | --- | --- |
    | uf_code_number | int | False | 1 | The code number of the state. |
    | data_only | bool | False | True | If `True`, returns only the data. If `False`, returns the data and the status
      code.
    |

    The function `generation_vehicle_brand` returns a dictionary with the following keys:

    | Key | Type | Description |
    | --- | --- | --- |
    | data | str | The generated data. |
    | status_code | int | The status code. |

    :param uf_code_number: The state code number, defaults to 1
    :type uf_code_number: int (optional)
    :param data_only: If True, the result will be a dictionary with the data only. If False, the result will be a
    dictionary with the data and the status code, defaults to True
    :type data_only: bool (optional)
    :return: A list of vehicle brands.
    """
    result = generation.generation_vehicle_brand(uf_code_number, data_only)
    return data_result(result)


@app.get("/api/generation-vehicle-plate")
async def generation_vehicle_plate(uf_code: str = '', formatting: bool = True, data_only: bool = True) -> {}:
    """
    It generates a vehicle plate number.

    :param uf_code: The state code for which you want to generate the license plate
    :type uf_code: str
    :param formatting: If True, the function will return the result with the formatting of the vehicle plate, defaults
    to True
    :type formatting: bool (optional)
    :param data_only: If True, the function will return only the data, if False, it will return the data and the
    formatting, defaults to True
    :type data_only: bool (optional)
    :return: A dictionary with the following keys:
        - uf_code: The UF code of the vehicle plate
        - uf_name: The UF name of the vehicle plate
        - vehicle_plate: The vehicle plate
        - formatting: The formatting of the vehicle plate
        - data_only: The data only of the vehicle plate
    """
    result = generation.generation_vehicle_plate(uf_code, formatting, data_only)
    return data_result(result)


@app.get("/api/generation-voter-title")
async def generation_voter_title(uf_code: str, data_only: bool = True) -> {}:
    """
    `generation_voter_title(uf_code: str, data_only: bool = True) -> {}`

    The first parameter is `uf_code` and it's a string. The second parameter is `data_only` and it's a boolean.
    The function returns a dictionary

    :param uf_code: The state code
    :type uf_code: str
    :param data_only: If True, the result will be a dictionary with the data only. If False, the result will be a
    dictionary with the data and the metadata, defaults to True
    :type data_only: bool (optional)
    :return: The result is a dictionary with the following structure:
    {
        "data": [
            {
                "uf": "AC",
                "title": "18-24",
                "voters": "12.9"
            },
            {
                "uf": "AC",
                "title": "25-34",
                "voters":
    """
    result = generation.generation_voter_title(uf_code, data_only)
    return data_result(result)


@app.post("/api/validator-cpf")
async def validators_cpf(validator_cpf: ValidatorsCpf):
    """
    It takes a ValidatorsCpf object as input, calls the generation.validators_cpf function, and returns the result as a
    JSON object

    :param validator_cpf: The CPF to be validated
    :type validator_cpf: ValidatorsCpf
    :return: The result of the function validators_cpf.
    """

    result = validators.validators_cpf(validator_cpf)
    return data_result(result)


@app.post("/api/validator-bank-account")
async def validators_bank_account(validator_bank_account: ValidatorsBankAccount):
    """
    `validators_bank_account` validates a validator's bank account

    :param validator_bank_account: ValidatorsBankAccount
    :type validator_bank_account: ValidatorsBankAccount
    :return: The result of the validators.validators_bank_account function.
    """
    result = validators.validators_bank_account(validator_bank_account)
    return data_result(result)


@app.post("/api/validator-certificate")
async def validators_certificate(validator_certificate: ValidatorsCertificate):
    """
    `validators_certificate` takes a `ValidatorsCertificate` object and returns a `DataResult` object

    :param validator_certificate: ValidatorsCertificate
    :type validator_certificate: ValidatorsCertificate
    :return: The result of the validators.validators_certificate function.
    """
    result = validators.validators_certificate(validator_certificate)
    return data_result(result)


@app.post("/api/validator-cnh")
async def validators_cnh(validator_cnh: ValidatorsCNH):
    """
    It validates the cnh.

    :param validator_cnh: The CNH number to be validated
    :type validator_cnh: ValidatorsCNH
    :return: The result of the validation of the cnh.
    """
    result = validators.validators_cnh(validator_cnh)
    return data_result(result)


@app.post("/api/validator-cnpj")
async def validators_cnpj(validator_cnpj: ValidatorsCNPJ):
    """
    It validates the CNPJ number.

    :param validator_cnpj: CNPJ to be validated
    :type validator_cnpj: ValidatorsCNPJ
    :return: The result of the validation of the CNPJ.
    """
    result = validators.validators_cnpj(validator_cnpj)
    return data_result(result)


@app.post("/api/validator-credit-card")
async def validators_credit_card(validator_credit_card: ValidatorsCreditCard):
    """
    It validates the credit card number.

    :param validator_credit_card: The credit card number to be validated
    :type validator_credit_card: ValidatorsCreditCard
    :return: A data result object.
    """
    result = validators.validators_credit_card(validator_credit_card)
    return data_result(result)


@app.post("/api/validator-pis-pasep")
async def validators_pis_pasep(validator_pis_pasep: ValidatorsPisPasep):
    """
    It validates the PIS / PASEP number.

    :param validator_pis_pasep: The PIS / PASEP number to be validated
    :type validator_pis_pasep: ValidatorsPisPasep
    :return: The result of the validation of the PIS / PASEP.
    """
    result = validators.validators_pis_pasep(validator_pis_pasep)
    return data_result(result)


@app.post("/api/validator-renavam")
async def validators_renavam(validator_renavam: ValidatorsRenavam):
    """
    It validates the renavam number.

    :param validator_renavam: Renavam number
    :type validator_renavam: ValidatorsRenavam
    :return: The result of the validation of the renavam.
    """
    result = validators.validators_renavam(validator_renavam)
    return data_result(result)


@app.post("/api/validator-rg")
async def validators_rg(validator_rg: ValidatorsRg):
    """
    It returns the validators of the given validator_rg.

    :param validator_rg: ValidatorsRg
    :type validator_rg: ValidatorsRg
    :return: The result of the validators_rg function.
    """
    result = validators.validators_rg(validator_rg)
    return data_result(result)


@app.post("/api/validator-state-registration")
async def validators_state_registration(validator_state_registration: ValidatorsStateRegistration):
    """
    `validators_state_registration` is a function that takes a `ValidatorsStateRegistration` object and returns a
    `DataResult` object.

    :param validator_state_registration: ValidatorsStateRegistration
    :type validator_state_registration: ValidatorsStateRegistration
    :return: The result of the validators_state_registration function.
    """
    result = validators.validators_state_registration(validator_state_registration)
    return data_result(result)


@app.post("/api/validator-voter-title")
async def validators_voter_title_code(validator_voter_title_code: ValidatorsVoterTitle):
    """
    `validators.validators_voter_title_code(validator_voter_title_code)`

    :param validator_voter_title_code: ValidatorsVoterTitle
    :type validator_voter_title_code: ValidatorsVoterTitle
    :return: The result of the validator_voter_title_code function.
    """
    result = validators.validators_voter_title_code(validator_voter_title_code)
    return data_result(result)


@app.get("/api/uf-codes")
async def get_uf_codes():
    """
    It returns a list of all the uf codes
    :return: A list of all the uf codes
    """
    result = consts.get_all_uf_code()
    return data_result(result)


@app.get("/api/bank-flags")
async def get_all_bank_flags():
    """
    It returns all the bank flags.
    :return: A list of all bank flags.
    """
    result = consts.get_all_bank_flags()
    return data_result(result)


@app.get("/api/uf-codes-two")
async def get_all_bank_flags_two():
    """
    It returns a list of all bank flags.
    :return: A list of all bank flags two.
    """
    result = consts.get_all_bank_flags_two()
    return data_result(result)


@app.get("/api/vehicle-brand")
async def get_all_vehicle_brands():
    """
    It returns a list of all vehicle brands
    :return: A list of all vehicle brands.
    """
    result = consts.get_all_vehicle_brands()
    return data_result(result)
