from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return f'{self.id} {self.name}'


class Category(models.Model):
    HOME_CHOICE = 'Home'
    WORK_CHOICE = 'Work'
    NAME_CHOICE = (
        (HOME_CHOICE, 'Home stuff'),
        (WORK_CHOICE, 'Work stuff'),
    )
    name = models.CharField(
        max_length=30,
        choices=NAME_CHOICE,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} {self.name}'


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )
    state = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True,

    )

    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title
