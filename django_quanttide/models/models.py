"""
数据模型
"""

from django.db import models


class Model(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
