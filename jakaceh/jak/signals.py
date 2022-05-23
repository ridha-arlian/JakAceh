# from .models import *
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def Create_User_Profile(sender, instance, created, **kwargs):
#     if created:
#         created = Profile.objects.get_or_create(user=instance)


# @receiver(post_save, sender= User)
# def Save_User_Profile(sender, instance, **kwargs):
#     instance.profile.save()        