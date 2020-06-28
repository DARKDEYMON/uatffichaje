from django import forms
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS

class fichas_form(forms.ModelForm):
	class Meta:
		model = fichas
		exclude = ['atendido']
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
	"""
	def __init__(self, *args, **kwargs):
		super(fichas_form, self).__init__(*args, **kwargs)
		self.fields['fecha'].widget.attrs = {'hidden':'true'}
	"""