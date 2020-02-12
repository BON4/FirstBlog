from django.dispatch import receiver
from .models import User
from django.db.models.signals import (post_save, post_delete)
from.task import one_sending
from django.shortcuts import reverse


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_verified:
            text_to_send = 'Follow this link to verify your account: http://127.0.0.1:8000%s' \
                           % reverse('users-verify', kwargs={'uuid': str(instance.verification_uuid)})

            one_sending(subject="Account verification",
                        text=text_to_send,
                        email=instance.email)
            print("Message must been sent")


@receiver(post_delete, sender=User)
def user_delete_signal(sender, instance, **kwargs):
    print('User has been deleted')
