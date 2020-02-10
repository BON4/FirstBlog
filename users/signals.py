from django.dispatch import receiver
from .models import User
from django.db.models.signals import (post_save, post_delete)


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, *args, **kwargs):
    print("Message must been sent")
    if created:
        if not instance.is_verified:
            # Реализовать ассинхронную отправку писем
            print("Message must been sent")


@receiver(post_delete, sender=User)
def user_delete_signal(sender, instance, **kwargs):
    print('User has been deleted')
