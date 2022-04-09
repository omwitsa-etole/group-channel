from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Channel
from django.dispatch import reciever

@reciever(post_save, sender=User)
def create_channel(sender, instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance)
        
@reciever(post_save, sender=User)
def save_channel(sender, instance, **kwargs):
    instance.channel.save()