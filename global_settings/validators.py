import json

from global_settings.choices import DICT, LIST, INT, FLOAT, STRING


def validate_list(value: str):
    data_list = json.loads(value)
    if not isinstance(data_list, list):
        raise TypeError('Value must be a list', value)
    return data_list


def validate_dict(value: str):
    data_list = json.loads(value)
    if not isinstance(data_list, dict):
        raise TypeError('Value must be a dictionary', value)
    return data_list


FUNCTION_KEY = {
    DICT: validate_dict,
    LIST: validate_list,
    INT: int,
    FLOAT: float,
    STRING: str,
}
