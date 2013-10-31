import django.forms.models

import test_formsets.models


class AuthorForm(django.forms.models.ModelForm):
	class Meta:
		model = test_formsets.models.Author
		fields = ['name']
	

BookInlineFormSet = django.forms.models.inlineformset_factory(
		test_formsets.models.Author,
		test_formsets.models.Book,
		fields=['title'],
		extra=1,
		)
