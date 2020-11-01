from django.shortcuts import render, redirect
from .models import short_url
from URLHandler.models import shorturl
import random
import string
from django.contrib import messages

# Create your views here.
def home_shortener(request, short=None):
    if not short or short == None:
        return render(request, 'form.html')
    else:
        url = short_url.objects.get(short_Query=short)
        return render(request, "form.html", {"url": url})


def randomGenerator():
    return ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(6))


def short_generate(request):
    if request.method == 'POST':
        if request.POST.get('original') and request.POST.get('short'):
            original = request.POST['original']
            short = request.POST['short']
            check1 = short_url.objects.filter(short_Query=short)
            check2 = shorturl.objects.filter(shortQuery=short)
            if not check1 and not check2:
                newURL = short_url(
                    original_URL=original,
                    short_Query=short,
                )
                newURL.save()
                return home_shortener(request,short)
            else:
                messages.error(request, 'Already Exists.')
                return redirect(home_shortener)
        elif request.POST.get('original'):
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomGenerator()
                check1 = short_url.objects.filter(short_Query=short)
                check2 = shorturl.objects.filter(shortQuery=short)
                if not check1 and not check2:
                    newURL = short_url(
                        original_URL=original,
                        short_Query=short,
                    )
                    newURL.save()
                    return home_shortener(request,short)
                else:
                    continue
        else:
            messages.error(request, 'Empty Fields.')
            return redirect('/')
    else:
        return redirect('/')
