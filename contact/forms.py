from django import forms

from contact.models import ContactModel, AboutUsModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ["created_at"]


class AboutUsModelForm(forms.ModelForm):
    class Meta:
        model = AboutUsModel
        exclude = ["created_at"]