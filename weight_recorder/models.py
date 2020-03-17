from django.db import models


class Weight(models.Model):
    weight_value = models.FloatField(verbose_name="Peso", blank=False)
    weight_date = models.DateField(
        "Data do registro", blank=False)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now=False, auto_now_add=True)
    insert_by = models.ForeignKey(
        "auth.User", verbose_name="Usuário", on_delete=models.CASCADE, blank=False)

    class Meta:
        verbose_name = "Peso"
        ordering = ("weight_date",)

    def __str__(self):
        return f"{self.insert_by.username} ({self.weight_value}Kg)"
