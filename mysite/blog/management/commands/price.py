import csv

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Calc price'

    def handle(self, *args, **options):
        reader = csv.DictReader(open("/../../../calculations_table.csv"))
        total_price = {}

        for row in reader:
            if row['Travel Method'] in ('Train', 'Plane'):
                if row['Resort Name'] in total_price:
                    total_price[row['Resort Name']] += int(row['Price'][1:].replace(',', ''))
                else:
                    total_price[row['Resort Name']] = int(row['Price'][1:].replace(',', ''))

        print(total_price)




