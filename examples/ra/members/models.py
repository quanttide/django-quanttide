from django_quanttide import models as quanttide_models


class Member(quanttide_models.Model):
    org_user_id = quanttide_models.IDField(primary_key=False, verbose_name='组织用户ID')
