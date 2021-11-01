from django.db import models


class House(models.Model):
    SQFT = 'SqFt'
    SQM = 'Sqm'
    AREA_UNIT_CHOICES = [
        (SQFT, 'Square Feet'),
        (SQM, 'Square Meters'),
    ]

    SINGLE_FAMILY = 'SingleFamily'
    DUPLEX = 'Duplex'
    HOME_TYPE_CHOICES = [
        (SINGLE_FAMILY, 'Single Family'),
        (DUPLEX, 'Duplex'),
    ]

    area_unit = models.CharField(
        max_length=8, choices=AREA_UNIT_CHOICES, default=SQFT,
    )
    bathrooms = models.DecimalField(
        decimal_places=1, max_digits=4, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    home_type = models.CharField(
        max_length=32, choices=HOME_TYPE_CHOICES, default=SINGLE_FAMILY,
    )
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.DecimalField(
        decimal_places=2, max_digits=32, blank=True, null=True)
    link = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=32)
    property_size = models.IntegerField(blank=True, null=True)
    rent_price = models.DecimalField(
        decimal_places=2, max_digits=32, blank=True, null=True)
    rentzestimate_amount = models.DecimalField(
        decimal_places=2, max_digits=32, blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.DecimalField(
        decimal_places=2, max_digits=32, blank=True, null=True)
    tax_year = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    zestimate_amount = models.DecimalField(
        decimal_places=2, max_digits=32, blank=True, null=True)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    zillow_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.IntegerField()
