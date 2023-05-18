from django.db import models

# Create your models here.
class Person(models.Model):
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    name = models.CharField(max_length=25)
    invitation = models.ForeignKey('Invitation', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Invitation'
        verbose_name_plural = 'Invitations'

    def __str__(self):
        return self.created_at
