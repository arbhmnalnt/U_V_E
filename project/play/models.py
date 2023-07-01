import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeStampMixin(models.Model):
    is_deleted      = models.BooleanField (default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'number'):
            if self.number != None:
                return 'جهاز رقم :' + str(self.number)
            else:
                return str("object")
            # return self.name
        elif hasattr(self, 'rent'):
            return str(self.id)
        elif hasattr(self, 'device'):
            return str(self.id)
        else:
            return str(self.id)



class Device(TimeStampMixin,models.Model):
    KIND = (
        ('P3','بلايستيشن 3'),
        ('P4','بلايستيشن 4'),
        ('P5','بلايستيشن 5')
    )
    number      = models.SmallIntegerField(null=True, blank=True)
    kind        = models.CharField(max_length=2, choices=KIND, default='P4',null=True, blank=True)
    price       = models.SmallIntegerField(null=True, blank=True, verbose_name='سعر ساعة الحجز', default=30)
    place       = models.CharField(max_length=50, null=True, blank=True)
    notes       = models.CharField(max_length=250,null=True, blank=True)
    available   = models.BooleanField(default=True, null=True, blank=True) 

class Rent(TimeStampMixin, models.Model):
    device          = models.ForeignKey('Device', on_delete=models.CASCADE, null=True, blank=True)
    duration        = models.IntegerField(null=True, blank=True, verbose_name='مدة الحجز بالدقائق')
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE)
    endTime         = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
            if (self.duration is not None or self.duration != 0) and self.created_at is not None:
                duration_in_minutes = datetime.timedelta(minutes=self.duration)
                self.endTime = self.created_at + duration_in_minutes
            super().save(*args, **kwargs)

class Order(TimeStampMixin, models.Model):
    rent    = models.ForeignKey('Rent', on_delete=models.CASCADE, null=True, blank=True)
    name    = models.CharField(max_length=75 ,null=True, blank=True, verbose_name='الطلب')
    amount = models.SmallIntegerField(null=True, blank=True, verbose_name='العدد')
    price   = models.IntegerField(null=True, blank=True, verbose_name='السعر')
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE)
   
