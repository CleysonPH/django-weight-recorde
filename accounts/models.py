from weight_recorder.views import weight_create
from django.db import models


class UserProfile(models.Model):
    profile_image = models.ImageField(
        verbose_name="Foto de perfil", upload_to="profile_image/%d/%m/%Y", blank=True)
    height = models.FloatField("Altura", blank=True)
    weight_goal = models.FloatField("Meta de peso", blank=True)
    user = models.ForeignKey(
        "auth.User", verbose_name="Usuário", on_delete=models.CASCADE, blank=False)
