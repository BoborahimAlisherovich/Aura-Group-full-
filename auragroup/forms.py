from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactUs, CareerApplication, ServicesDetails


class ContactForm(forms.ModelForm):
    """Aloqa formasi"""
    class Meta:
        model = ContactUs
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("To'liq ismingiz")
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Telefon raqamingiz")
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _("Email manzilingiz")
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _("Xabaringizni yozing..."),
                'rows': 4
            }),
        }


class ServicesDetailsForm(forms.ModelForm):
    """Xizmat so'rovi formasi"""
    class Meta:
        model = ServicesDetails
        fields = [
            'company_name',
            'phone_number',
            'contact_name',
            'description',
            'email',
            'telegram',
            'file',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Kompaniya nomi")
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Telefon raqam (+998...)")
            }),
            'contact_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Aloqa uchun ism")
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _("Loyiha haqida qisqacha ma'lumot..."),
                'rows': 4
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _("Email (ixtiyoriy)")
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Telegram username (ixtiyoriy)")
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.zip'
            }),
        }


class CareerApplicationForm(forms.ModelForm):
    """Vakansiya arizasi formasi"""
    class Meta:
        model = CareerApplication
        fields = [
            'full_name',
            'message',
            'file',
            'telegram',
            'phone_number'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("To'liq ismingiz")
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _("O'zingiz haqingizda qisqacha..."),
                'rows': 4
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Telegram username")
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Telefon raqamingiz")
            }),
        }
