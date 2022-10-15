from pydantic import BaseModel


# A class that validates the CPF number.
class ValidatorsCpf(BaseModel):
    cpf_code: str
    data_only: bool = True


# > This class is a model for the validators_rg table
class ValidatorsRg(BaseModel):
    rg_code: str
    data_only: bool = True


# > This class is a validator for the BankAccount model
class ValidatorsBankAccount(BaseModel):
    bank: int
    agency: str
    account: str
    data_only: bool = True


# > This class is used to validate the certificate of a validator
class ValidatorsCertificate(BaseModel):
    certificate_code: str
    data_only: bool = True


# A class that inherits from the BaseModel class.

class ValidatorsCNH(BaseModel):
    cnh_code: str
    data_only: bool = True


# A class that validates the CNPJ.

class ValidatorsCNPJ(BaseModel):
    cnpj_code: str
    data_only: bool = True


# > This class validates credit card numbers.

class ValidatorsCreditCard(BaseModel):
    flag: int
    credit_card_code: str
    data_only: bool = True


# A class that validates the PIS / PASEP number.

class ValidatorsPisPasep(BaseModel):
    pis_pasep_code: str
    data_only: bool = True


# > This class is responsible for validating the Renavam number

class ValidatorsRenavam(BaseModel):
    renavam_code: str
    data_only: bool = True


# > This class is used to validate the title of a voter.

class ValidatorsVoterTitle(BaseModel):
    voter_title_code: str
    data_only: bool = True


# > This class is used to validate the state registration number of a company

class ValidatorsStateRegistration(BaseModel):
    uf_code: str
    state_registration_code: str
    data_only: bool = True
