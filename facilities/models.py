from django.db import models

class Facility(models.Model):
    facilityId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images//%Y/%m/%d', blank=True)
    contactNumber = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = 'Facilities'
        ordering = ('-facilityId',)

    def __str__(self):
        return self.name

    objects = models.Manager()



class FacilityStaff(models.Model):
    userName = models.CharField(max_length=200, blank=False, null=False, unique=True)
    password = models.CharField(max_length=200, blank=False, null=False, unique=True)
    admin = models.BooleanField(default=False)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Facility Staffs'
    
    def __str__(self):
        return self.userName
    
    objects = models.Manager()


class FacilityAdmin(models.Model):
    userName = models.CharField(max_length=200, blank=False, null=False, unique=True)
    password = models.CharField(max_length=200, blank=False, null=False, unique=True)
    admin = models.BooleanField(default=False)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='facility_admins')
    staff = models.ManyToManyField(FacilityStaff)

    class Meta:
        verbose_name_plural = 'Facility Admins'

    def __str__(self):
        return self.userName
    
    objects = models.Manager()