from URLHandler.models import shorturl
from django.http import JsonResponse
from home_shorty.models import short_url
from home_shorty.views import randomGenerator
import json


# Create your views here.

def short_generate(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
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
                    return JsonResponse({'original': original, 'short': f"https://srty.me/{short}"})
                else:
                    return JsonResponse({'error': 'The custom url is already used.'})
            elif request_data['original']:
                original = request_data['original']
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
                        return JsonResponse({'original': original, 'short': f"https://srty.me/{short}"})
                    else:
                        continue
        except Exception:
            return JsonResponse({'error': 'Empty Fields'})
    else:
        return JsonResponse({'message': 'Please provide original and(or) custom url to shorten(or customise). '})
