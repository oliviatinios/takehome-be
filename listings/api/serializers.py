from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField()

    class Meta:
        model = House
        fields = [
            "id",
            "area_unit",
            "bathrooms",
            "bedrooms",
            "home_size",
            "home_type",
            "last_sold_date",
            "last_sold_price",
            "link",
            "price",
            "property_size",
            "rent_price",
            "rentzestimate_amount",
            "rentzestimate_last_updated",
            "tax_value",
            "tax_year",
            "year_built",
            "zestimate_amount",
            "zestimate_last_updated",
            "zillow_id",
            "address",
            "city",
            "state",
            "zipcode",
        ]
        extra_kwargs = {
            "last_sold_date": {"required": False},
            "last_sold_price": {"required": False},
            "rent_price": {"required": False},
            "rentzestimate_amount": {"required": False},
            "rentzestimate_last_updated": {"required": False},
            "tax_value": {"required": False},
            "tax_year": {"required": False},
            "zestimate_amount": {"required": False},
            "zestimate_last_updated": {"required": False},
            "zillow_id": {"required": False},
            "year_built": {"required": False},
            "home_size": {"required": False},
            "propert_size": {"required": False},
            "bathrooms": {"required": False},
            "bedrooms": {"required": False},
        }
