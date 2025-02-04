from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# View for user registration

# define a function named register that takes a single argument request, 
# which represents the HTTP request received from the client.
def register(request):
    # check if the request method is POST. If it is, the user has submitted the registration form.
    if request.method == 'POST':
        # create an instance of UserCreationForm and passes the data submitted in the form 
        # (contained in request.POST) to the form.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If the form data is valid save the form data to the database and create
            # a new user account. The newly created user object is assigned to the variable user
            user = form.save()
            login(request, user)
            # After successfully registering and logging in the user, redirect the user to the home page.
            return redirect('home')
    else:
        form = UserCreationForm()
    # renders the register.html template, passing the form instance (form) as context. 
    # This allows the template to display the form to the user.
    return render(request, 'accounts/register.html', {'form': form})