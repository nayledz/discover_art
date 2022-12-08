from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from discover_art.art_accounts.models import Account

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Account(
            user=instance,
        )
        profile.save()


@receiver(pre_save, sender=Account)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.age:
        instance.is_complete = True

