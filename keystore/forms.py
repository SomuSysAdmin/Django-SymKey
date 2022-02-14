from django import forms
from .models import Credential
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CredsCreateForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['tag', 'username']
        
    # Most of the code in this class (below) if from UserCreationForm, but modified to fit a non-User model and has had _post_clean removed.
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        cred = super().save(commit=False)
        cred.set_password(self.cleaned_data["password1"])
        if commit:
            cred.save()
        return cred
