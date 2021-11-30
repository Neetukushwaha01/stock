from django.db import models
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Stack(models.Model):
    stock_name =models.CharField(max_length=100)
    video=models.FileField(upload_to="uploads/video", null=True, blank=True)
    desc =models.TextField(max_length=1200,null=True,blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)


@receiver(pre_save, sender=Stack)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)