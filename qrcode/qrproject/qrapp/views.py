from django.shortcuts import render
from django.http import JsonResponse
import qrcode
import os
from django.conf import settings

def index(request):
    return render(request,'index.html')

# 

def generate_qr(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print('url:',url)
        if not url:
            return JsonResponse({'error': 'Please provide a URL'})
        
    
        qr = qrcode.make(url)
        qr_path = os.path.join(settings.BASE_DIR, 'static', 'qr.png')
        
     
        qr.save(qr_path)
        print('qr_url:', settings.STATIC_URL + 'qr.png') 
        qr_url = os.path.join(settings.STATIC_URL, 'qr.png')
        return render(request, 'index.html',  {'qr_url': qr_url})

    return render(request, 'index.html')