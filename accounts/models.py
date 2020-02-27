from django.db import models

from weight_recorder.models import Weight


class UserProfile(models.Model):
    profile_image = models.ImageField(
        verbose_name="Foto de perfil", default="default.png", upload_to="profile_image/%d/%m/%Y", blank=False, null=False)
    height = models.FloatField("Altura", blank=True, null=True)
    weight_goal = models.FloatField("Meta de peso", blank=True, null=True)
    user = models.OneToOneField(
        "auth.User", verbose_name="Usuário", on_delete=models.CASCADE, blank=False, null=False)

    def get_imc(self):
        if not self.height:
            return 0
        weights = Weight.objects.filter(insert_by=self.user)
        weight = weights.latest('weight_date')
        return weight.weight_value / self.height ** 2
