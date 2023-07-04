"""
模型层字段
"""

import uuid

from django.db import models


class IDField(models.UUIDField):
    """
    ID字段

    微服务系统内全局唯一。

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
    """
    标识字段

    租户内同模型唯一。

    用于表示名称或标题的标识符字段，通常用于生成URL Slug。

    :param max_length: 字段允许的最大长度，默认为100个字符。
    :type max_length: int
    :param unique: 字段的值是否在整个模型中唯一，默认为True。
    :type unique: bool
    :param verbose_name: 字段的可读名称，默认为“标识”。
    :type verbose_name: str
    """
    description = "标识字段"

    def __init__(self, **options):
        # ChatGPT建议的值是50-70，这里取了一个稍大的值。
        options.setdefault('max_length', 100)
        options.setdefault('unique', True)
        options.setdefault('verbose_name', '标识')
        super().__init__(**options)


class VerboseNameField(models.CharField):
    """
    名称字段

    :param max_length: 字段允许的最大长度，默认为100个字符。
    :type max_length: int
    :param default: 字段的默认值，默认为空字符串。
    :type default: str
    :param blank: 如果为True，则该字段允许为空值，默认为True。
    :type blank: bool
    :param null: 如果为True，则该字段允许为NULL值，默认为True。
    :type null: bool
    :param verbose_name: 字段的可读名称，默认为“标题”。
    :type verbose_name: str
    """
    description = "名称字段"

    def __init__(self, **options):
        options.setdefault('max_length', 100)
        options.setdefault('default', None)
        options.setdefault('blank', True)
        options.setdefault('null', True)
        options.setdefault('verbose_name', '标题')
        super().__init__(**options)


class TitleField(models.CharField):
    """
    标题字段

    :param max_length: 字段允许的最大长度，默认为255个字符。
    :type max_length: int
    :param default: 字段的默认值，默认为空字符串。
    :type default: str
    :param blank: 如果为True，则该字段允许为空值，默认为True。
    :type blank: bool
    :param null: 如果为True，则该字段允许为NULL值，默认为True。
    :type null: bool
    :param verbose_name: 字段的可读名称，默认为“标题”。
    :type verbose_name: str
    """
    description = "标题字段"

    def __init__(self, **options):
        options.setdefault('max_length', 255)
        options.setdefault('default', None)
        options.setdefault('blank', True)
        options.setdefault('null', True)
        options.setdefault('verbose_name', '标题')
        super().__init__(**options)


class DescriptionField(models.TextField):
    """
    描述字段

    :param default: 字段的默认值，默认为空字符串。
    :type default: str
    :param blank: 如果为True，则该字段允许为空值，默认为True。
    :type blank: bool
    :param null: 如果为True，则该字段允许为NULL值，默认为True。
    :type null: bool
    :param verbose_name: 字段的可读名称，默认为“描述”。
    :type verbose_name: str
    """
    description = "描述字段"

    def __init__(self, **kwargs):
        kwargs.setdefault('default', None)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('null', True)
        kwargs.setdefault('verbose_name', '描述')
        super().__init__(**kwargs)
