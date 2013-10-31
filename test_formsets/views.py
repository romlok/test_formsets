from django.forms.models import modelformset_factory
from django.views import generic

from test_formsets import models
from test_formsets import forms


class TestView(generic.TemplateView):
	""" Displays an author and their books """
	template_name = 'author.html'
	
	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		
		author = models.Author.objects.get(pk=1)
		form = forms.AuthorForm(instance=author)
		book_formset = forms.BookInlineFormSet(instance=author)
		
		context['form'] = form
		context['book_formset'] = book_formset
		context['book_form_meta'] = book_formset.forms[0]._meta
		
		return context
		
	
