#در قسمت لاگین یه قسمت برای سیگنال گذاشته شده که وقتی یوزر ساخته شد پروفایلش هم ساخته بشه و اگه یوزر وار استراک بود پروفایل وار استراک ساخته بشه و اگه یوزر هوم اونر بود پروفایل هوم اونر ساخته بشه
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User_war_struck, User_home_owner

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'war_struck':
            User_war_struck.objects.create(user=instance, Job_title='Default')
        elif instance.user_type == 'home_owner':
            User_home_owner.objects.create(user=instance, Job_title='Default')