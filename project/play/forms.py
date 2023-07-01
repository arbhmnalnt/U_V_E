from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from .models import Device, Rent, Order
from django.contrib.auth.models import User
import datetime
from django.utils import timezone



class RentForm(forms.ModelForm):
    device = forms.ModelChoiceField(queryset=Device.objects.all(), label='الجهاز')
    duration = forms.IntegerField(label='المدة المحجوزة (بالدقائق) / 0 - مفتوح')
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), label='تم الحجز بواسطة')

    class Meta:
        model = Rent
        fields = ['device', 'duration']
        labels = {
            'device': 'رقم الجهاز',
            'duration': 'مدة الحجز بالدقائق / 0 - مفتوح',
            'created_by': 'تم الحجز بواسطة'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        if self.user:
            self.initial['created_by'] = self.user.username
    
    def save(self, commit=True):
        rent = super().save(commit=False)
        self.created_at = timezone.now()
        if self.cleaned_data['duration'] != 0:
            rent.endTime =  self.created_at + datetime.timedelta(minutes=self.cleaned_data['duration'])
        if commit:
            rent.save()
        return rent

class OrderForm(forms.ModelForm):
    rent     = forms.ModelChoiceField(queryset=Rent.objects.all(), widget=forms.Select(), label='الحجز')
    name     = forms.CharField(widget=forms.TextInput, label='اسم الصنف')
    amount   = forms.IntegerField(widget=forms.NumberInput(), label='العدد')
    price    = forms.IntegerField(widget=forms.NumberInput(), label='اجمالى السعر')
    
    class Meta:
        model = Order
        fields = ['rent', 'name', 'amount', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.user = kwargs.pop('user', None)
        self.helper.layout = Layout(
            Field('rent'),
            Field('name'),
            Field('amount'),
            Field('price'),
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        if self.user:
            self.initial['created_by'] = self.user.username

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order
