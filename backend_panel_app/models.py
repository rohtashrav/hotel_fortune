from django.db import models


class UserRole(models):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.role_name
    