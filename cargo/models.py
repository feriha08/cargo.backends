from django.db import models

class Cargo(models.Model):
    load_number = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=15)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    load_type = models.CharField(max_length=50)
    recipient_name = models.CharField(max_length=100)
    recipient_phone = models.CharField(max_length=15)
    is_received = models.BooleanField(default=False)
    received_by = models.CharField(max_length=100, null=True, blank=True)
    identification_number = models.CharField(max_length=100, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.load_number

        
