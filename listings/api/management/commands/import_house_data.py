from django.core.management.base import BaseCommand, CommandError
from api.models import House
import csv


PRICE_MULTIPLIER = {
    'M': 1000000,
    'K': 100000,
}


def convert_price_string_with_units_to_float(price_string):
    if not price_string:
        return None
    unit = price_string[-1]
    value = float(price_string[1:-1])
    return value * PRICE_MULTIPLIER[unit]


def convert_string_to_float(price_string):
    if not price_string:
        return None
    if '.' in price_string:
        return float(price_string)
    return float(int(price_string))


def convert_string_to_int(string):
    return int(string) if string else None


def convert_date_format(date):
    if date == '':
        return None
    date_parts = date.split('/')
    return '{}-{}-{}'.format(date_parts[2], date_parts[0], date_parts[1])


class Command(BaseCommand):
    help = 'Imports data about houses'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, newline='') as csvfile:
            model_count = 0

            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert price from formatted string (e.g. '$2.9M') to float
                price_float = convert_price_string_with_units_to_float(
                    row['price'])

                # Convert strings to float
                last_sold_price_float = convert_string_to_float(
                    row['last_sold_price'])
                rent_price_float = convert_string_to_float(
                    row['rent_price'])
                rentzestimate_amount_float = convert_string_to_float(
                    row['rentzestimate_amount'])
                zestimate_amount_float = convert_string_to_float(
                    row['zestimate_amount'])
                tax_value_float = convert_string_to_float(
                    row['tax_value'])
                bathrooms_float = convert_string_to_float(row['bathrooms'])

                # Convert strings to int or float
                home_size_int = convert_string_to_int(row['home_size'])
                property_size_int = convert_string_to_int(
                    row['property_size'])
                year_built_int = convert_string_to_int(row['year_built'])
                tax_year_int = convert_string_to_int(row['tax_year'])
                bedrooms_int = convert_string_to_int(row['bedrooms'])
                zillow_id_int = convert_string_to_int(row['zillow_id'])

                # Convert dates from MM/DD/YYYY to YYYY-MM-DD format
                formatted_last_sold_date = convert_date_format(
                    row['last_sold_date'])
                formatted_rentzestimate_last_updated = convert_date_format(
                    row['rentzestimate_last_updated'])
                formatted_zestimate_last_updated = convert_date_format(
                    row['zestimate_last_updated'])

                # Create house model for row of csv data
                house = House(
                    area_unit=row[' area_unit'][1:],
                    bathrooms=bathrooms_float,
                    bedrooms=bedrooms_int,
                    home_size=home_size_int,
                    home_type=row['home_type'],
                    last_sold_date=formatted_last_sold_date,
                    last_sold_price=last_sold_price_float,
                    link=row['link'],
                    price=price_float,
                    property_size=property_size_int,
                    rent_price=rent_price_float,
                    rentzestimate_amount=rentzestimate_amount_float,
                    rentzestimate_last_updated=formatted_rentzestimate_last_updated,
                    tax_value=tax_value_float,
                    tax_year=tax_year_int,
                    year_built=year_built_int,
                    zestimate_amount=zestimate_amount_float,
                    zestimate_last_updated=formatted_zestimate_last_updated,
                    zillow_id=zillow_id_int,
                    address=row['address'],
                    city=row['city'],
                    state=row['state'],
                    zipcode=row['zipcode']
                )

                # Save house model
                house.save()
                model_count += 1
                self.stdout.write(
                    'Saving house model {} to db'.format(model_count))
