from django import forms

class userform(forms.Form):
      
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    no_of_travellers = forms.IntegerField(label="Enter no of travellers:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter no of travellers:', 'oninput': 'calculateUpdatedPrice()'}))
    cnic = forms.CharField(label="CNIC:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your CNIC'}))
    phone = forms.CharField(label="Phone Number:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Phone Number:'}))
    nationality = forms.CharField(label="Nationality:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Nationality:'}))
    total_amount = forms.DecimalField(label="Total Price:", widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    datetimeampm = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])

class account_details(forms.Form):
    account_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your account name'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your account number'}))
