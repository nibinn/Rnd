from django import forms
class CustomerForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class FOCPredictionForm(forms.Form):
	draft = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	age = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	stw_kn = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	model_sea_state_d = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	no_of_months_after_dry_dock = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	dwt = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

	