from django.db import models

class Stocks(models.Model):
    categories = models.CharField(max_length=34, blank=True,null=True)
    item_name = models.CharField(max_length=23, blank=True, null=True) 
    quantity = models.IntegerField(default='0', null=True,blank=True)
    receive_quantity = models.IntegerField(default='0', null=True, blank=True)
    received_by = models.CharField(max_length=45,blank=True,null=True)
    issue_quantity = models.IntegerField(default='0', null=True,blank=True)
    issue_by = models.CharField(max_length=56,blank=True,null=True)
    phone_number = models.CharField(max_length=46,blank=True,null=True) 
    created_by = models.CharField(max_length=23,blank=True,null=True)
    recorded_level = models.IntegerField(default='0', null=True,blank=True)
    last_update = models.DateTimeField(auto_now_add=False,auto_now=True)
    export_to_CSV = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.item_name} {str(self.quantity)}'         