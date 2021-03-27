from URLHandler.models import shorturl
from django.http import JsonResponse
from home_shorty.models import short_url
from home_shorty.views import randomGenerator
import json
import string
from random import choice
from .models import APIKey
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

UPPERCASE = list(string.ascii_uppercase)
LOWECASE = string.ascii_lowercase
NUMBER = string.digits
SYMBOLS = ['@', '#', '$', '%', '&', '_']
API_LIMIT = 100


# Create your views here.

def create_api():
    data = list(UPPERCASE) + list(LOWECASE) + list(NUMBER) + SYMBOLS
    key = ''.join(choice(data) for _ in range(30))
    api_key = 'Shorty.'+key
    print(api_key)
    return api_key


def send_api(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            name = request_data['name']
            user_email = request_data['email']
            if APIKey.objects.filter(email=user_email).exists():
                return JsonResponse({'api_duplicate': True})
            api_key = create_api()
            new_key = APIKey(name=name, email=user_email, api_key=api_key)
            new_key.save()
            data = {
                'name': name.capitalize(),
                'api_key': api_key
            }
            html_content = render_to_string("email.html", data)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                f"API Key | Shorty",
                text_content,
                "Shorty <no-reply@srty.me>",
                [user_email]
            )
            print("sending email")
            email.attach_alternative(html_content, "text/html")
            try:
                email.send()
                print("Sent")
                return JsonResponse({'api_success': True})
            except Exception as e:
                print(e)
                return JsonResponse({'api_error': True})

        except Exception as e:
            print(e)
            return JsonResponse({'api_error': True})


def short_generate(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            if request_data.get('api_key'):
                api_key = request_data['api_key']
                try:
                    api = APIKey.objects.get(api_key=api_key)
                except APIKey.DoesNotExist:
                    return JsonResponse({'error': 'Invalid API Key'})
                if api.usage < API_LIMIT:
                    if request_data.get('original') and request_data.get('short'):
                        original = request_data['original']
                        short = request_data['short']
                        check1 = short_url.objects.filter(short_Query=short)
                        check2 = shorturl.objects.filter(shortQuery=short)
                        if not check1 and not check2:
                            newURL = short_url(
                                original_URL=original,
                                short_Query=short,
                            )
                            newURL.save()
                            api.usage += 1
                            api.save()
                            return JsonResponse({'original': original, 'short': f"https://srty.me/{short}"})
                        else:
                            return JsonResponse({'error': 'The custom url is already used.'})
                    elif request_data['original']:
                        original = request_data['original']
                        generated = False
                        while not generated:
                            short = randomGenerator()
                            check1 = short_url.objects.filter(
                                short_Query=short)
                            check2 = shorturl.objects.filter(shortQuery=short)
                            if not check1 and not check2:
                                newURL = short_url(
                                    original_URL=original,
                                    short_Query=short,
                                )
                                newURL.save()
                                api.usage += 1
                                api.save()
                                return JsonResponse({'original': original, 'short': f"https://srty.me/{short}"})
                            else:
                                continue
                else:
                    api.expired = True
                    api.save()
                    return JsonResponse({'error': 'API Key usage limit exceeded'})
            else:
                return JsonResponse({'error': 'API Key not provided'})
        except Exception:
            return JsonResponse({'error': 'Empty Fields'})
    else:
        return JsonResponse({'message': 'Please provide original and(or) custom url to shorten(or customise). '})
