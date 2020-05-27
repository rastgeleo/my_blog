from django import forms
from django.core.mail import mail_managers, BadHeaderError
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):

    email = forms.EmailField(
        initial='youremail@domail.com'
        )
    subject = forms.CharField(max_length=63)
    text = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        email = self.cleaned_data.get('email')
        subject = self.cleaned_data.get('subject')
        text = self.cleaned_data.get('text')
        body = 'Message From: {}\n\n{}'.format(email, text)

        try:
            mail_managers(subject, body)
        except BadHeaderError:
            self.add_error(
                None,
                ValidationError(
                    'Could not send the Email.'
                    'Extra headers not allowed in email body.',
                    code='badheader')
                )
            return False
        return True
