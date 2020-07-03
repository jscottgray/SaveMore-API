from django.db import models


class Product(models.Model):
    sku = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    PRODUCE = 'PR'
    MEAT_ALTERNATIVES = 'MA'
    MEAT = 'ME'
    BEVERAGES = 'BE'
    BULK = 'BU'
    DELI = 'DE'
    SOUP = "SO"
    WORLD = "WO"
    CONDIMENTS = "CO"
    SNACKS = "SN"
    PASTA = "PA"
    FROZEN = "FR"
    BAKERY = "BA"
    BAKING = "BK"
    BREAKFAST = "BF"
    WELLNESS = "WE"
    BABY = "BB"
    CLEANING = "CL"
    BEER = "BR"
    NO_CATEGORY = "NO"
    DEPARTMENT_CHOICES = [
        (PRODUCE, 'Produce'),
        (MEAT_ALTERNATIVES, 'Meat Alternatives'),
        (MEAT, 'ME'),
        (BEVERAGES, 'BE'),
        (BULK, 'BU'),
        (DELI, 'DE'),
        (SOUP, "SO"),
        (WORLD, "WO"),
        (CONDIMENTS, "CO"),
        (SNACKS, "SN"),
        (PASTA, "PA"),
        (FROZEN, "FR"),
        (BAKERY, "BA"),
        (BAKING, "BK"),
        (BREAKFAST, "BF"),
        (WELLNESS, "WE"),
        (BABY, "BB"),
        (CLEANING, "CL"),
        (BEER, "BR"),
        (NO_CATEGORY, "NO")
    ]
    department = models.CharField(
        max_length=2,
        choices=DEPARTMENT_CHOICES,
        default=NO_CATEGORY,
    )


class Price(models.Model):
    # not setting primary key as Django only supports a single column primary key
    # Django will auto-create a column ID as the primary key
    sku = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    multibuy = models.BooleanField()
    sales_description = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
