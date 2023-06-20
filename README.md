# Global Settings Django App

The "global_settings" Django app is designed to handle global settings and configuration variables for your Django
project. It provides a convenient way to manage and access global settings throughout your application.

## Features

- Centralized management of global settings and configuration variables.
- Easy integration into your Django project.
- Access global settings anywhere within your application.
- Different types of variables. (dict, list, int, float, str)

## Installation

1. Install the "global_settings" app using pip:

```shell
pip install global_settings
```

2. Add "global_settings" to your Django project's `INSTALLED_APPS` setting in the project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'global_settings',
    ...
]
```

3. Run database migrations to create the necessary database tables:

```shell
python manage.py migrate
```

4. You're ready to start using the "global_settings" app in your Django project!

## Usage

1. Create and manage global settings:

   The "global_settings" app provides a Django admin interface to manage global settings. You can access it by
   navigating to `/admin/global_settings/` in your project.

2. Access global settings in your code:

   You can access global settings anywhere in your Django application by importing the `global_settings` module and
   using the `get_global_setting` function:

   ```python
   from global_settings.utils import get_global_setting

   setting_value = get_global_setting('SETTING_NAME')
   ```

   Replace `'SETTING_NAME'` with the name of the setting you want to retrieve, and `default_value` with the default
   value to be used if the setting doesn't exist.

   Note: Make sure to import the `get_global_setting` function from the `global_settings.utils` module.

## Configuration

The "global_settings" app provides a few configuration options that can be set in your project's `settings.py` file:

- `GLOBAL_SETTINGS_DEFAULT_VALUES`: (optional) Define default values that are user when `get_global_setting` is called.

To set these configuration options, add them to your project's `settings.py` file:

```python
import json
from global_settings.choices import INT, FLOAT, STRING, LIST, DICT

GLOBAL_SETTINGS_DEFAULT_VALUES = {
    'A': {
        'value': 1,
        'type': INT
    },
    'B': {
        'value': 'test string',
        'type': STRING
    },
    'C': {
        'value': 1,
        'type': FLOAT
    },
    'D': {
        'value': json.dumps([1, 2, 3, 4]),
        'type': LIST
    },
    'E': {
        'value': json.dumps({
            'key1': 1,
            'key2': {
                'key2.1': 1,
                'key2.2': 'test string'
            },
            'key3': [1, 'test', 1.3]
        }),
        'type': DICT,
    },
}

```

## Contributing

Contributions to the "global_settings" app are welcome! If you find any issues or have suggestions for improvements,
please feel free to open an issue or submit a pull request on the GitHub
repository: [link-to-repo](https://github.com/your/repo)

## License

The "global_settings" app is open-source and released under the [MIT License](https://opensource.org/licenses/MIT).