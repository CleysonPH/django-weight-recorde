from django.db import models


class Weight(models.Model):
    weight_value = models.FloatField(verbose_name="Peso")
    created_at = models.DateTimeField(
        verbose_name="Data de Criação", auto_now=False, auto_now_add=True)
    insert_by = models.ForeignKey(
        "auth.User", verbose_name="Usuário", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.insert_by.username} ({self.weight_value}Kg)"
