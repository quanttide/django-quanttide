from django_quanttide import models


class ExampleNumberModel(models.Model):
    number = models.NumberField()


class ExampleModel(models.Model):
    number = models.NumberField()
    name = models.NameField()
    verbose_name = models.VerboseNameField()
    title = models.TitleField()
    description = models.DescriptionField()
    type = models.TypeField(choices=[('book', 'Book'), ('movie', 'Movie'), ('music', 'Music')], default='book')
    status = models.StatusField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft')
    stage = models.StageField()
    created_at = models.CreatedAtField()
    updated_at = models.UpdatedAtField()

    class Meta:
        verbose_name = '示例模型'
        verbose_name_plural = '示例模型列表'


class BaseParentModel(models.PolymorphicModel):
    class Meta:
        abstract = True


class BaseChildModel(models.PolymorphicModel):
    class Meta:
        abstract = True


class ParentModel(BaseParentModel):
    pass


class ChildModel(ParentModel):
    pass
