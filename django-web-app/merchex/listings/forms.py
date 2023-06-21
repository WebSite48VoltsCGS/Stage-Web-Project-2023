from django import forms
from listings.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
    group = forms.CharField(max_length=100, required=False)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=1000)
    confirm_password = forms.CharField(max_length=1000)

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SignForm(forms.Form):
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)

    def __init__(self, *args, **kwargs):
        super(SignForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
