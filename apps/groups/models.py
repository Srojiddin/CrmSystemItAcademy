from django.db import models

class Group(models.Model):
    title = models.CharField(
        max_length=420,
        verbose_name = "nazvaniy gruppi",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="data sozdaniya",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "gruppa"
        verbose_name_plural = "gruppi"
    
