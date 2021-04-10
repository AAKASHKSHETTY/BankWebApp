from django.db import models

class detail(models.Model):
   name = models.CharField(max_length=100)
   Cust_id = models.CharField(max_length=100)
   location = models.CharField(max_length=10,default='')
   Amount = models.IntegerField(default= 0)
   img = models.ImageField(upload_to='pictures')

   def __str__(self):
      return self.title

class trans(models.Model):
   payer_id = models.CharField(max_length=100)
   payee_id = models.CharField(max_length=100)
   trans_amt = models.IntegerField(default= 0)

   def __str__(self):
      return self.title

