from django import forms

class NoteForm(forms.Form):
	title = forms.CharField(max_length = 40,
		widget = forms.TextInput(
			attrs = {'placeholder': 'Title', 
					'style': 'width: 100%; font-size: 20px;',
					}))
	content = forms.CharField(max_length = 1000,
		widget = forms.Textarea(
			attrs = {'placeholder': 'Content', 
					'style': 'width: 100%; font-size: 20px;',
					}))