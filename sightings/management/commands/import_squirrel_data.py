import csv
from django.core.management import BaseCommand
from dateutil import parser
from sightings.models import Squirrel
from datetime import date
import re

class Command(BaseCommand):
    help = 'This command Imports the squirrel.csv file into our database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')

        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader)
            unique_id = list()
            for row in reader:
                if row[2] in unique_id:
                    continue
                else:
                    month, day, year = pattern.match(row[5]).groups()
                    squirrel = Squirrel.objects.get_or_create(
                        Latitude = float(row[0]),
                        Longitude = float(row[1]),
                        Unique_Squirrel_ID = row[2],
                        Shift = row[4],
                        Date = date(int(year), int(month), int(day)),
                        Age = row[7],
                        Primary_Fur_Color = row[8],
                        Location = row[12],
                        Specific_Location = row[14],
                        Running = True if row[15] == 'TRUE' else False,
                        Chasing = True if row[16] == 'TRUE' else False,
                        Climbing = True if row[17] == 'TRUE' else False,
                        Eating = True if row[18] == 'TRUE' else False,
                        Foraging = True if row[19] == 'TRUE' else False,
                        Other_Activities = True if row[20] == 'TRUE' else False,
                        Kuks = True if row[21] == 'TRUE' else False,
                        Quaas = True if row[22] == 'TRUE' else False,
                        Moans = True if row[23] == 'TRUE' else False,
                        Tail_flags = True if row[24] == 'TRUE' else False,
                        Tail_twitches = True if row[25] == 'TRUE' else False,
                        Approaches = True if row[26] == 'TRUE' else False,
                        Indifferent = True if row[27] == 'TRUE' else False,
                        Runs_from = True if row[28] == 'TRUE' else False
                    )
                    unique_id.append(row[2])
