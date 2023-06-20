"""
模型层字段
"""

import uuid

from django.db import models


class IDField(models.UUIDField):
    """
    ID字段

    默认作为主键使用；
    不作为主键使用时，设置`primary_key=False`，并建议自定义`verbose_name`。
    """
    def __init__(self, **options):
        options['primary_key'] = options.get('primary_key', True)
        options['editable'] = options.get('editable', not options['primary_key'])
        options['default'] = options.get('default', uuid.uuid4)
        options['verbose_name'] = options.get('verbose_name', 'ID')
        super().__init__(**options)


class NameField(models.SlugField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class VerboseNameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
