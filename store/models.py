from account.models import Account

from django.db      import models


class Store(models.Model):
    name            = models.CharField(max_length = 50)
    store_code      = models.CharField(max_length = 50)
    phone_number    = models.CharField(max_length = 50)
    longitude       = models.DecimalField(max_digits = 50, decimal_places = 7, null = True)
    latitude        = models.DecimalField(max_digits = 50, decimal_places = 7, null = True)
    distance        = models.DecimalField(max_digits = 50, decimal_places = 3, null = True)
    street_name     = models.CharField(max_length = 200)
    district        = models.ForeignKey('District', on_delete = models.CASCADE, null = True)
    city            = models.ForeignKey('City', on_delete = models.CASCADE, null = True)
    business_time   = models.ForeignKey('BusinessTime', on_delete = models.CASCADE, null = True)
    account         = models.ManyToManyField(Account, through = 'FavoriteStore')
    service_one     = models.ManyToManyField('ServiceOne', through = 'StoreServiceOne')
    service_two     = models.ManyToManyField('ServiceTwo', through = 'StoreServiceTwo')

    class Meta:
        db_table = 'stores'

    def __str__(self):
        return self.name

class ServiceOne(models.Model):
    name            = models.CharField(max_length = 50) 
    code            = models.CharField(max_length = 20, null = True)
    icon_url        = models.URLField(max_length = 2000, null = True)
    thumbnail_url   = models.URLField(max_length = 2000, null = True)
    description = models.TextField(null = True)

    class Meta:
        db_table = 'services_one'

class ServiceTwo(models.Model):
    name            = models.CharField(max_length = 50) 
    code            = models.CharField(max_length = 20, null = True)
    icon_url        = models.URLField(max_length = 2000, null = True)
    thumbnail_url   = models.URLField(max_length = 2000, null = True)
    description     = models.TextField(null = True)

    class Meta:
        db_table = 'services_two'

    def __str__(self):
        return self.name

class StoreServiceOne(models.Model):
    store   = models.ForeignKey(Store, on_delete = models.CASCADE)
    service = models.ForeignKey(ServiceOne, on_delete = models.CASCADE)

    class Meta:
        db_table = 'stores_services_one'

class StoreServiceTwo(models.Model):
    store   = models.ForeignKey(Store, on_delete = models.CASCADE)
    service = models.ForeignKey(ServiceTwo, on_delete = models.CASCADE)

    class Meta:
        db_table = 'stores_services_two'

class District(models.Model):
    name    = models.CharField(max_length = 50)
    city    = models.ForeignKey('City', on_delete = models.CASCADE, null=True)

    class Meta:
        db_table = 'districts'

    def __str__(self):
        return self.name

class City(models.Model):
    name    = models.CharField(max_length = 50)

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name

class BusinessTime(models.Model):
    time    = models.CharField(max_length = 50)

    class Meta:
        db_table = 'business_times'

    def __str__(self):
        return self.time

class FavoriteStore(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE, null = True)
    store   = models.ForeignKey(Store, on_delete = models.CASCADE, null = True)

    class Meta:
        db_table = 'favorite_stores'
