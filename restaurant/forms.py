from django import forms

from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ("name", "email", "phone", "message")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "autocomplete": "name",
                    "placeholder": "Your full name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "autocomplete": "email",
                    "placeholder": "you@email.com",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "autocomplete": "tel",
                    "placeholder": "09xx xxx xxxx (optional)",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-textarea",
                    "rows": 5,
                    "placeholder": "Tell us about your event, order, or questions…",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].required = False
