from django.db import models

from apps.users.models import User

from apps.groups.models import Group


class Student(User):
    group = models.ForeignKey(
        Group,
        on_delete = models.SET_NULL,
        related_name= "students",
        verbose_name = "gruppa",
        null=True, blank=True,

    )
    full_name = models.CharField(
        max_length=51,
        verbose_name = "polnoe imya",

    )
    phone_number = models.CharField(
        max_length=17,
        verbose_name = "nomer telefona",
    )


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "studenti"