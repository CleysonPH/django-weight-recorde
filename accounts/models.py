from weight_recorder.views import weight_create
from django.db import models


class UserProfile(models.Model):
    profile_image = models.ImageField(
        verbose_name="Foto de perfil", default="default.png", upload_to="profile_image/%d/%m/%Y", blank=False, null=False)
    height = models.FloatField("Altura", blank=True, null=True)
    weight_goal = models.FloatField("Meta de peso", blank=True, null=True)
    user = models.OneToOneField(
        "auth.User", verbose_name="Usuário", on_delete=models.CASCADE, blank=False, null=False)
