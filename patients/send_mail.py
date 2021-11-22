from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from decouple import config
from datetime import datetime


def send_mail(self, event):
    if event == 'new':
        title = 'New Appointment Added'
    elif event == 'update':
        title = 'Appointment Updated'
    elif event == 'cancel':
        title = 'Appointment Cancelled'
    elif event == None:
        raise ValueError('No event passed.')
    else:
        raise ValueError('Invalid event passed.')

    title = f'Curewell - [{title}]'

    context = {
        'appointment': self,
        'appointment_edit':
        f'{config("HOST")}/admin/patients/appointment/{self.id}/change',
        'appointment_delete':
        f'{config("HOST")}/admin/patients/appointment/{self.id}/delete',
        'now': datetime.now().strftime('%d/%m/%Y %H:%M'),
    }
    print(context['now'])
    html_content = render_to_string("email_temp.html", context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        title,
        text_content,
        config('EMAIL_HOST_USER'),
        # test only.
        [config('EMAIL_HOST_USER')])
    email.attach_alternative(html_content, "text/html")
    email.send()
