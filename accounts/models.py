from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class ProfileAbstractModel(models.Model):
    phone = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=13, null=True)
    first_name = models.CharField(max_length=13, null=True)
    last_name = models.CharField(max_length=13, null=True)
    country = models.CharField(max_length=13, null=True)
    address1 = models.CharField(max_length=13, null=True)
    address2 = models.CharField(max_length=13, null=True, blank=True)
    city = models.CharField(max_length=13, null=True)
    postcode = models.CharField(max_length=13, null=True)

    class Meta:
        abstract = True


class ProfileModel(ProfileAbstractModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile: {str(self.user)}"

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profile"

