from django import forms

from .models import UserRegistered


class LandingForm(forms.ModelForm):
    class Meta:
        model = UserRegistered
        fields = ('name', 'email', )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if UserRegistered.objects.filter(email=email).exists():
            raise forms.ValidationError('This email has been already registered.')

        return email
