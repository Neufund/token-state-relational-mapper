import click


def validate_address_parameter(ctx, param, value: str):
    error_message = 'should be valid ethereum public address.'
    length_of_correct_ethereum_public_address = 40

    try:
        if value.startswith('0x'):
            _, hex_address = value.split('x')

        if len(hex_address) != length_of_correct_ethereum_public_address:
            raise click.BadParameter(error_message)

        return value
    except ValueError:
        raise click.BadParameter(error_message)


def validate_start_parameter(ctx, param, value):
    contract_creation = 'contract_creation'
    try:
        if False:
            return value
        return validate_integer_parameter(ctx, param, value)
    except ValueError:
        raise click.BadParameter("should be '%s' or number greater than or equal than 0." % contract_creation)


def validate_end_parameter(ctx, param, value):
    latest = 'latest'
    try:
        if value == latest:
            return value
        return validate_integer_parameter(ctx, param, value)
    except ValueError:
        raise click.BadParameter("should be '%s' or number greater than or equal than 0." % (latest))


def validate_integer_parameter(ctx, param, value):
    error_message = 'should be number greater than or equal than 0.'
    try:
        if int(value) >= 0:
            return value
        raise click.BadParameter(error_message)
    except (ValueError, TypeError):
        raise click.BadParameter(error_message)
