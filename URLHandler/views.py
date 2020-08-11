from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import shorturl
import random
import string

# Create your views here.
@login_required(login_url='/loginPage/')
def dashboard(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})
    
def randomGenerator():
    return ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(6))

@login_required(login_url='/loginPage/')
def generate(request):
    if request.method == 'POST':
        if request.POST['original'] and request.POST['short']:
            usr = request.user
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(shortQuery=short)
            if not check:
                newURL = shorturl(
                    user = usr,
                    orginalURL=original,
                    shortQuery = short,
                )
                newURL.save()
                return redirect(dashboard)
            else:
                messages.error(request, 'Already Exists.')
                return redirect(dashboard)
        elif request.POST['original']:
            usr = request.user
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomGenerator()
                check = shorturl.objects.filter(shortQuery=short)
                if not check:
                    newURL = shorturl(
                        user = usr,
                        originalURL=original,
                        shortQuery = short,
                    )
                    newURL.save()
                    return redirect(dashboard)
                else:
                    continue

        else:
            messages.error(request, 'Empty Fields.')
            return redirect(dashboard)
    else:
        return redirect('/dashboard')

def home(request, query=None):
    if not query or query == None:
        return render(request, 'home.html')
    else:
        try:
            check = shorturl.objects.get(shortQuery=query)
            check.visits += 1
            check.save()
            url_to_redirect = check.originalURL
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'home.html', {'error': 'Error'})
            
@login_required(login_url='/loginPage/')
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = shorturl.objects.filter(shortQuery=short)
            check.delete()
            return redirect(dashboard)
        except shorturl.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)
