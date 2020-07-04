from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'main_categories'

    def __str__(self):
        return self.name

class MenuBar(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(MainCategory, on_delete = models.CASCADE, null = True)

    class Meta:
        db_table = 'menu_bars'

    def __str__(self):
        return self.name

class Product(models.Model):
    name_kr         = models.CharField(max_length = 50)
    name_en         = models.CharField(max_length = 50, null = True)
    price           = models.CharField(max_length = 50, null = True)
    icecream_option = models.CharField(max_length = 10, null = True)
    description     = models.CharField(max_length = 200, null = True)
    thumbnail       = models.CharField(max_length = 2500, null = True)
    release_date    = models.CharField(max_length = 30, null = True)
    menu            = models.ForeignKey('MenuBar', on_delete = models.CASCADE)
    nutrition       = models.ForeignKey('Nutrition', on_delete = models.SET_NULL, null = True)
    size            = models.ManyToManyField('Size', through = 'ProductSize')
    tag             = models.ManyToManyField('Tag', through = 'ProductTag')
    allergy         = models.ManyToManyField('Allergy', through = 'ProductAllergy')
    flavor          = models.ManyToManyField('self', through = 'ProductFlavor', symmetrical = False)
    rank            = models.IntegerField(null = True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name_kr

class ProductFlavor(models.Model):
    from_product    = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, related_name = 'from_product')
    to_product      = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, related_name = 'to_product')

    class Meta:
        unique_together = ('from_product', 'to_product')
        db_table        = 'products_flavors'

class Nutrition(models.Model):
    offer       = models.CharField(max_length = 200)
    calories    = models.CharField(max_length = 200)
    natrium     = models.CharField(max_length = 200)
    sugar       = models.CharField(max_length = 200)
    fat         = models.CharField(max_length = 200)
    protein     = models.CharField(max_length = 200)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        db_table = 'allergies'

    def __str__(self):
        return self.name

class ProductAllergy(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_allergies'

class Size(models.Model):
    name        = models.CharField(max_length = 50)
    price       = models.IntegerField(null = True)
    description = models.CharField(max_length = 50)

    class Meta:
        db_table = 'sizes'

class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    size    = models.ForeignKey('Size', on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_sizes'

class Tag(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    tag     = models.ForeignKey('Tag', on_delete = models.CASCADE, null = True)

    class Meta:
        db_table = 'products_tags'