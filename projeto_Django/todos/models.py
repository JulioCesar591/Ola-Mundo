from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de Início", null=False, blank=False)
    finished = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_complete(self):
        if not self.finished:
            self.finished = date.today()
            self.save()
