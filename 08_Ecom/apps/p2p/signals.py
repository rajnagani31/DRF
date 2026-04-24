import email
from os import error
import re

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete

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
        print('data:',instance.password )
        "send welcom email to user and stored user data"
        welcom_email_service(instance.email)
    else:
        print(f"User {instance.username} has been updated, no welcome email sent.")


# Test pre save with logic
@receiver(pre_save, sender=User)
def validate_user_email(sender, instance, **kwargs):
    print("Signal triggered: pre_save for User checking email validity")
    if instance.email == 'test@123.com':
        raise ValueError("Invalid email address: 'test@123.com' is not a valid email.")
    else:
        print(f"Email {instance.email} is valid for user {instance.username}.")

# Test pre delete if any email is not sended then stop delete user
@receiver(pre_delete, sender=User)
def prevent_user_deletion_if_email_not_sent(sender, instance, **kwargs):
    print("Signal triggered: pre_delete for User")
    unsent_emails = Email.objects.filter(email=instance.email, is_sended=False)

    if unsent_emails.exists():
        print(f"User {instance.username} has unsent emails. Deletion prevented.")
        raise ValueError(f"Cannot delete user {instance.username} because there are unsent emails associated with this user.")
    else:
        print(f"User {instance.username} has no unsent emails. Deletion allowed.")  

# Post delete for delere unsended email data from DB

@receiver(post_delete, sender= User)
def delete_unsended_email_data(sender, instance, **kwargs):
    print("Signal triggered: post_delete for delete all unsended email data")
    data = Email.objects.filter(is_sended=False).delete()
    if data:
        print("Unsended email data deleted successfully")
    else:
        print("No unsended email data found")   

