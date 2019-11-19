from django import forms
from .models import Vendor, VendorAddress


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels = {
            'name': 'Vendor Name',
            'email': 'Vendor Email',
            'contact_no': 'Vendor Contact Number'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_no': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VendorAddrForm(forms.ModelForm):
    class Meta:
        model = VendorAddress
        fields = '__all__'

        exclude = ['vendor_id',]
        labels = {
            'vendor_addr': 'Vendor Address',
        }
        widgets = {
            'vendor_addr': forms.Textarea(attrs={'class': 'form-control'})
        }
