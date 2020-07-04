from django.db import models

class Account(models.Model):
    name       = models.CharField(max_length = 50)
    email      = models.EmailField(max_length = 50, unique = True)
    password   = models.CharField(max_length = 300)
    address    = models.CharField(max_length = 300)
    phone      = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'accounts'
