from pydantic import BaseModel
import dataclasses


# A class that validates the CPF number.
@dataclasses.dataclass(init=False)
class ValidatorsCpf(BaseModel):
    cpf_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is a model for the validators_rg table
@dataclasses.dataclass(init=False)
class ValidatorsRg(BaseModel):
    rg_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is a validator for the BankAccount model
@dataclasses.dataclass(init=False)
class ValidatorsBankAccount(BaseModel):
    bank: int = dataclasses.field()
    agency: str = dataclasses.field()
    account: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is used to validate the certificate of a validator
@dataclasses.dataclass(init=False)
class ValidatorsCertificate(BaseModel):
    certificate_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# A class that inherits from the BaseModel class.
@dataclasses.dataclass(init=False)
class ValidatorsCNH(BaseModel):
    cnh_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# A class that validates the CNPJ.
@dataclasses.dataclass(init=False)
class ValidatorsCNPJ(BaseModel):
    cnpj_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class validates credit card numbers.
@dataclasses.dataclass(init=False)
class ValidatorsCreditCard(BaseModel):
    flag: int = dataclasses.field()
    credit_card_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# A class that validates the PIS / PASEP number.
@dataclasses.dataclass(init=False)
class ValidatorsPisPasep(BaseModel):
    pis_pasep_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is responsible for validating the Renavam number
@dataclasses.dataclass(init=False)
class ValidatorsRenavam(BaseModel):
    renavam_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is used to validate the title of a voter.
@dataclasses.dataclass(init=False)
class ValidatorsVoterTitle(BaseModel):
    voter_title_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)


# > This class is used to validate the state registration number of a company
@dataclasses.dataclass(init=False)
class ValidatorsStateRegistration(BaseModel):
    uf_code: str = dataclasses.field()
    state_registration_code: str = dataclasses.field()
    data_only: bool = dataclasses.field(default=True)
