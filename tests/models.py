from django_quanttide import models


class ExampleModel(models.Model):
    name = models.NameField()
    verbose_name = models.VerboseNameField()
    title = models.TitleField()
    description = models.DescriptionField()
    type = models.TypeField(choices=[('book', 'Book'), ('movie', 'Movie'), ('music', 'Music')], default='book')
    status = models.StatusField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='draft')
    stage = models.StageField()

    class Meta:
        verbose_name = '示例模型'
        verbose_name_plural = '示例模型列表'


class ExamplePolymorphicModel(models.PolymorphicModel):
    TYPE_FIELD_MAPPINGS = {
        'ExamplePolymorphicModel': 'default',
        'ChildModel': 'child_model'
    }


class ChildModel(ExamplePolymorphicModel):
    pass
