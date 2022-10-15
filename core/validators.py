import fordev

from baseModel.base_model import (ValidatorsCpf, ValidatorsRg, ValidatorsBankAccount, ValidatorsCertificate,
                                  ValidatorsCNH, ValidatorsCNPJ, ValidatorsCreditCard, ValidatorsPisPasep,
                                  ValidatorsRenavam, ValidatorsVoterTitle, ValidatorsStateRegistration)


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
