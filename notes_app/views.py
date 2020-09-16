from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from datetime import datetime

from .models import Note
from .forms import NoteForm


def index(request):
	notes_list = Note.objects.order_by('-id')

	# form =  TodoForm()

	context = {'notes_list': notes_list}
	return render(request, 'notes_app/index.html', context)

def add_note_editor(request):
	if request.method == 'GET':
		new_note = Note(title = '', content = '')

		form =  NoteForm()

		context = {'note' : new_note, 'form' : form, 'edit':False}
		return render(request, 'notes_app/editor.html', context)
	elif request.method == 'POST':
		form = NoteForm(request.POST )

		if form.is_valid():
			content = request.POST['content']
			content = content.replace('/n', '<br>')
			if len(content) > 500:
				size = 3
			elif len(content) > 200:
				size = 2
			else:
				size = 1
			new_note = Note(title = request.POST['title'], content = content, time = datetime.now().strftime("%H:%M %p"), size = size)
			new_note.save()

		return redirect('index')

def deleteNote(request, note_id):
	note = Note.objects.get(pk = note_id)
	note.delete()
	return redirect('index')

def editNote(request, note_id):
	if request.method == 'GET':
		note = Note.objects.get(pk = note_id)
		form =  NoteForm(initial = {'title': note.title, 'content': note.content})
		context = {'note' : note, 'form' : form, 'edit': True}
		print(note.content)
		print(note.time)
		print(len(note.content))

		return render(request, 'notes_app/editor.html', context)
	elif request.method == 'POST':
		form = NoteForm(request.POST )
		note = Note.objects.get(pk = note_id)
		if form.is_valid():
			content = request.POST['content']
			content = content.replace('/n', '<br>')

			note.title = request.POST['title']
			note.content = content
			if len(content) > 500:
				size = 3
			elif len(content) > 200:
				size = 2
			else:
				size = 1
			note.size = size			
			note.time = datetime.now().strftime("%H:%M %p")
			note.save()
		return redirect('index')



# @require_POST
# def add_note(request):
# 	form = NoteForm(request.POST )

# 	if form.is_valid():
# 		new_note = ToDo(title = request.POST['title'], content = request.POST['content'])
# 		new_note.save()

# 	return redirect('index')


