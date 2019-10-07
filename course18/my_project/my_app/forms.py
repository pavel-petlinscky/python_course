from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    name = forms.CharField(label='Your name')
    message = forms.CharField(required=False)

    def clean_name(self):
        """auto magic of form validation
        """
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise ValidationError('Name is too short')

        return name

    def clean_message(self):
        """auto magic of form validation
        """
        message = self.cleaned_data['message']
        if len(message) <= 4:
            raise ValidationError('Message is too short')

        return message

    def clean(self):
        print('Cleaning self')
        if self.cleaned_data.get('name', None) == 'Ivan':
            raise ValidationError('NOOOO!')

        return self.cleaned_data
