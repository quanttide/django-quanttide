"""
模型层字段
"""

import uuid

from django.db import models


class IDField(models.UUIDField):
    """
    ID字段

    默认作为主键使用；
    不作为主键、作为关联ID使用时，设置`primary_key=False`，
    同时建议自定义`verbose_name`，格式为"<关联模型名称>ID"。

    :param primary_key: 是否作为主键，默认为True
    :type primary_key: bool
    :param editable: 是否可编辑，默认为非主键字段可编辑
    :type editable: bool
    :param default: 默认值，默认为uuid.uuid4
    :type default: callable
    :param verbose_name: 字段名称，默认为'ID'
    :type verbose_name: str
    """
    description = 'ID字段'

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
