from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# In-memory lists to store names (will reset on server restart)
firstnamesorted = []  # First names list
lastnamesorted = []  # Last names list

# Combined form for both first and last names
class CombinedNameForm(forms.Form):
    # Field names here must match keys used in cleaned_data below
    firstnamesorted = forms.CharField(label='First Name', max_length=100)
    lastnamesorted = forms.CharField(label='Last Name', max_length=100)

# Index view: displays all names
def index(request):
    # Passes lists to template as 'firstnames' and 'lastnames'
    return render(request, 'sortedname/index.html', {
        'firstname': firstnamesorted,
        'lastname': lastnamesorted
    })

# Add view: handles form submission for new names
def add(request):
    if request.method == 'POST':
        form = CombinedNameForm(request.POST)
        # Validate form
        if form.is_valid():
            # Get values from form
            firstname = form.cleaned_data['firstnamesorted']  # Must match field name above
            lastname = form.cleaned_data['lastnamesorted']    # Must match field name above
            # Add to lists
            firstnamesorted.append(firstname)
            lastnamesorted.append(lastname)
            # Redirect to index after adding
            return HttpResponseRedirect(reverse('sortedname:index'))
        else:
            # If form is invalid, re-render with errors
            return render(request, 'sortedname/add.html', {
                'form': form
            })
    else:
        # GET request: show empty form
        return render(request, 'sortedname/add.html', {
            'form': CombinedNameForm()
        })
