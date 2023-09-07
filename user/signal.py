from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(costumer =instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwags):
    instance.profile.save()