from os import error
import re

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, profile, Blog, Email



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("Signal triggered: post_save for User")
    if created:
        profile.objects.create(
            user=instance,
            bio=f"Updated bio for {instance.username}",
        )

# Triggerred before saving a blog -> runing before saving in database
@receiver(pre_save, sender=Blog)
def before_saving_blog(sender, instance, **kwargs):
    print("signal triggered: pre_save for Blog->" + instance.title)


# Triggerred after saving a blog -> runing after saving in database
@receiver(post_save, sender=Blog)
def after_saving_blog(sender, instance, created, **kwargs):
    print("signal triggered: post_save for Blog->" + instance.title)
    if created:
        print("A new blog has been created with title: " + instance.title)
    else:
        print("An existing blog has been updated with title: " + instance.title)

# welcom email service


def welcom_email_service(email):
    print(f"Sending welcome email to {email}...")
    Email.objects.create(email=email, is_sended=True)
    print(f"Welcome email sent to {email} successfully!")


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        "send welcom email to user and stored user data"
        welcom_email_service(instance.email)
    else:
        print(f"User {instance.username} has been updated, no welcome email sent.")

