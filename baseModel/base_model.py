from pydantic import BaseModel


# A class that validates the CPF number.
class ValidatorsCpf(BaseModel):
    cpf_code: str
    data_only: bool
