from django.conf import settings
from django.core.exceptions import ValidationError

from global_settings.choices import TYPE_CHOICES


def get_global_setting(name):
    """
    Get the data from model GlobalSettings.

    Args:
        name: name of variable in admin of GlobalSettings model

    Returns: Return a dict containing the data to be used

    """
    from global_settings.models import GlobalSettings
    value = GlobalSettings.get_value_if_exist(name)
    if value is not None:
        return value

    default_config = getattr(settings, 'GLOBAL_SETTINGS_DEFAULT_VALUES', {})
    if name not in default_config:
        return

    var_type = default_config[name]['type']
    if var_type not in dict(TYPE_CHOICES).keys():
        raise ValidationError('Type "{}" if not valid'.format(var_type))

    return create_global_settings(GlobalSettings, name, default_config).get_formatted_value()


def create_global_settings(global_settings_model, name, default_config):
    """
    Creates a global settings object using the provided global_settings_model and default configuration.

    Args:
        global_settings_model: The model used to create the global settings object.
        name (str): The name of the global setting.
        default_config (dict): The default configuration containing the value and type of the global setting.

    Returns:
        global_settings_model: The created global settings object.

    Raises:
        ValidationError if data is to save is wrong
    """
    global_settings = global_settings_model(
        name=name,
        value=default_config[name]['value'],
        type=default_config[name]['type'],
    )
    global_settings.full_clean()
    global_settings.save()
    return global_settings
