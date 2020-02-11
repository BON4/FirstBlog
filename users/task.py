from celery import shared_task, task
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.shortcuts import reverse
from smtplib import SMTPException


@shared_task(bind=True, autoretry_for=(SMTPException,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def one_sending(self, subject, text, email):
    try:
        send_mail(
            subject=subject,
            message=text,
            from_email='silvia.homam@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
    except BadHeaderError:
        print("Program found a newline character. This is injection defender exception !")
