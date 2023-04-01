from django.db import models
from django.urls import reverse_lazy


class TreeMenu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child',
    )
    url = models.CharField(max_length=255, unique=True)
    named_url = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs) -> None:
        context = {'slug': self.url}
        self.url = reverse_lazy('menu', kwargs=context)
        super(TreeMenu, self).save()

    def __str__(self) -> models.CharField:
        return self.name
