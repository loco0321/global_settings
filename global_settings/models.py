import sys

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from global_settings.choices import TYPE_CHOICES, STRING
from global_settings.validators import FUNCTION_KEY


class GlobalSettings(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField(blank=True, null=True, help_text="save the value with json.dumps'")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default=STRING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Global Settings'
        verbose_name_plural = 'Global Settings'

    @classmethod
    def get_value_if_exist(cls, name):
        try:
            instance = GlobalSettings.objects.get(name=name)
            return instance.get_formatted_value()
        except GlobalSettings.DoesNotExist:
            return None

    def get_formatted_value(self):
        return FUNCTION_KEY[self.type](self.value)

    def clean(self):
        super(GlobalSettings, self).clean()
        try:
            FUNCTION_KEY[self.type](self.value)
        except (KeyError, IndexError, ValueError, TypeError):
            etype, exc, _ = sys.exc_info()
            raise ValidationError('Unable to parse value specified with formatted, {0}: {1}'.format(etype, exc))

    def save(self, **kwargs):
        self.name = slugify(self.name or '').replace('-', '_').upper()
        super(GlobalSettings, self).save(**kwargs)

    def __str__(self):
        return self.name
