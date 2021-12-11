from django.core.management.base import BaseCommand, CommandError
from umblake.models import Instrument_group, Instrument, Events, Departments
from django.core import serializers
import sys

class Command(BaseCommand):
    
    #def add_arguments(self, parser):
    #    parser.add_argument('test', nargs='+', type=int)

    def handle(self, *args, **options):
        start = 0
        size = 500
        list_model = [Instrument_group, Instrument, Events, Departments]
        for model in list_model:
          #model = Instrument_group
          count = model.objects.using('user').count()
          print("%s objects in model %s" % (count, model))
          for i in range(start, count, size):
             print(i)
             sys.stdout.flush()
             original_data =  model.objects.using('user').all()[i:i+size]
             original_data_json = serializers.serialize("json", original_data)
             new_data = serializers.deserialize("json", original_data_json, 
                                             using='default')
             #for n in original_data:
             for n in new_data:
                n.save(using='default')
                print(n)  
