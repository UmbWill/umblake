from django.db import models

class Instrument_group(models.Model):

   name = models.CharField(max_length = 50)
   order_number = models.IntegerField()
   version = models.IntegerField()
   is_deleted = models.IntegerField()
   updated_at = models.DateTimeField()
   updated_by= models.CharField(max_length = 50)
   created_at = models.DateTimeField()  
   created_by = models.CharField(max_length = 50)

   class Meta:
      db_table = "instrument_group"


class Instrument(models.Model):

   id = models.CharField(max_length=1000, primary_key=True)
   name = models.CharField(max_length = 50)
   instrument_group_id = models.IntegerField() 
   count = models.IntegerField() 
   effective_start = models.DateField(null=True)
   effective_end = models.DateField(null=True)
   order_number = models.IntegerField()
   version = models.IntegerField()
   is_deleted = models.IntegerField()   
   updated_at = models.DateTimeField()
   updated_by= models.CharField(max_length = 50)
   created_at = models.DateTimeField()  
   created_by = models.CharField(max_length = 50,null=True)

   class Meta:
      db_table = "instrument"

class Events(models.Model):

   id = models.CharField(max_length=10000000, primary_key=True)
   message_header_id= models.IntegerField()
   patient_number= models.CharField(max_length = 50)   
   patient_name_kana= models.CharField(max_length = 50)
   patient_name= models.CharField(max_length = 50)
   is_inpatient= models.CharField(max_length = 50)
   gender= models.CharField(max_length = 50)  
   birthday= models.CharField(max_length = 50)
   order_number = models.BigIntegerField()
   event_type= models.CharField(max_length = 50) 
   event_datetime= models.CharField(max_length = 50)
   ope_room_name= models.CharField(max_length = 50) 
   ope_order_date= models.CharField(max_length = 50)
   section_code= models.CharField(max_length = 50)
   gaia_pid= models.CharField(max_length = 50)  
   section_name= models.CharField(max_length = 50) 
   disease_name= models.CharField(max_length = 50) 
   pre_operation_name= models.CharField(max_length = 50)
   surgeon_doctor= models.CharField(max_length = 50)
   assistant= models.CharField(max_length = 50)  
   anesth_doctor= models.CharField(max_length = 50)      
   operation_name= models.CharField(max_length = 50)     
   ope_room_name_from= models.CharField(max_length = 50) 
   event_note= models.CharField(max_length = 50)
   gw_received_at= models.DateTimeField() 
   gw_updated_at= models.DateTimeField()
   
   class Meta:
      db_table = "events"

class Departments(models.Model):
   
   IF_INDT  = models.DateTimeField()
   IF_UPDT = models.DateTimeField() 
   IF_SEQ = models.BigIntegerField(primary_key=True)
   IF_STT= models.DateTimeField() 
   IF_PMD  = models.CharField(max_length = 50) 
   HOSPITALCODE = models.CharField(max_length = 50)
   DEPTCODE  = models.CharField(max_length = 50) 
   DEPTNAME  = models.CharField(max_length = 50) 
   DEPTSHORTNAME = models.CharField(max_length = 50)  
   DEPTSPECIALNAME = models.CharField(max_length = 50,null=True)
   DEPTSTATUS = models.CharField(max_length = 50)   
   RECEDEPTCODE  = models.CharField(max_length = 50)
   DEPTSEQ = models.IntegerField() 
   VISIBLESTATUS = models.CharField(max_length = 50,null=True)
 
   class Meta:
      db_table = "departments"

