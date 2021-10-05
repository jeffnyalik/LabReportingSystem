from django.db import models
from facilities.models import Facility
from authentication.models import Profile


STATUS = (
    ('Available', 'AVAILABLE'),
    ('Closed', 'CLOSED'),
)

PAYMENT_TYPE = (
    ('Full Payment', 'Full Payment'),
    ('Half Payment', 'Half Payment'),
)

PAYMENT_METHOD = (
    ('MPESA', 'Mpesa'),
    ('CREDIT CARD', 'Credit Card'),
    ('ON ARRIVAL', 'On Arrival'),
)

TIME_SLOT = (
    ('10:00 AM - 2:00 PM', '10:00 AM - 2:00 PM'),
    ('3:00 PM - 7:00 PM', '3:00 PM - 7:00 PM'),
    ('8:00 PM - 10:00 PM', '8:00 PM - 10:00 PM'),
)

class LabTest(models.Model):
    testId = models.AutoField(primary_key=True)
    testName = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=2, default=0)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='test_facility')
    image = models.ImageField(upload_to='images/test//%Y/%m/%d', blank=True)
    active_status = models.CharField(max_length=20, choices=STATUS, default='AVAILABLE')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 


    class Meta:
        verbose_name_plural = 'Lab Tests'
        ordering = ['-testId']

    def __str__(self):
        return self.testName

    objects = models.Manager()


class OrderTest(models.Model):
    orderId =  models.AutoField(primary_key=True)
    clientInfo = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='order_test_user')
    contactNumber = models.CharField(max_length=200, blank=True, null=True)
    testInfo = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, related_name='test_order')
    paymentType = models.CharField(max_length=20, choices=PAYMENT_TYPE, default='Full Payment', blank=True, null=True)
    paymentMethod = models.CharField(max_length=20, choices=PAYMENT_METHOD, blank=True, null=True)
    bookedTimeSlot = models.CharField(max_length=20, choices=TIME_SLOT, blank=True, null=True)
    bookedDate = models.DateField(blank=True, null=True)
    order_created_at = models.TimeField(auto_now=True)
    staffChecking = models.BooleanField(default=False)
    adminApprove = models.BooleanField(default=False)
    orderConfirmed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    validation = models.BooleanField(default=False)
    clientTested = models.BooleanField(default=False)

    class Meta:
        ordering = ['-orderId']

    def __str__(self):
        return self.testInfo.testName