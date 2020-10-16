import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'import data from the 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file',help='file containing squirrel amount details')

    def handle(self, *args, **options):
        file_=options['squirrel_file']

        with open(file_) as fp:
            reader=csv.DictReader(fp)

           # for item in reader:
            #    obj = SquirrelDetail()



        msg = f'You are importing from{file_}' 
        self.stdout.write(self.style.SUCCESS(msg))
