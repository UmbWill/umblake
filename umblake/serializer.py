import sys
from django.core import serializers
from djlake.umblake.models import Instrument_group
#DJANGO_SETTINGS_MODULE = 'lake.settings'

def migrate(model):
    size=500
    start=0
    print("%s model " $(model))
    #count = model.objects.using('user').count()
    #print("%s objects in model %s" % (count, model))
    #for i in range(start, count, size):
    #    print(i)
    #    sys.stdout.flush()
    #    original_data =  model.objects.using('user').all()[i:i+size]
    #    original_data_json = serializers.serialize("json", original_data)
    #    new_data = serializers.deserialize("json", original_data_json, 
    #                                       using='default')
    #    for n in new_data:
    #        n.save(using='default')

migrate(Instrument_group)
