from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
import os

# Import necessary image processing library (example: Pillow)
from PIL import Image, ImageEnhance

def index(request):
    if request.method == 'POST':
        # Handle image upload from request
        if 'original_image' not in request.FILES:
            return HttpResponseBadRequest('No image uploaded.')

        original_image = request.FILES['original_image']
        # Process image (example: brightness enhancement)
        image = Image.open(original_image)
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(1.5)  # Adjust brightness factor
        # Optionally, save enhanced image to media directory
        enhanced_image_filename = f'{original_image.name.split(".")[0]}_enhanced.jpg'
        enhanced_image_path = os.path.join(settings.MEDIA_ROOT, 'enhanced', enhanced_image_filename)
      # Assuming your template is 'home.html'
        enhanced_image.save(enhanced_image_path)

        # Prepare context for displaying original and enhanced images
        context = {
            'original_image_url': os.path.join(settings.MEDIA_URL, 'originals', original_image.name),
            'enhanced_image_url': os.path.join(settings.MEDIA_URL, 'enhanced', enhanced_image_filename),
        }
        return render(request, 'visualwizardApp/index.html',context)

    else:
        # Display homepage for initial image upload
        return render(request, 'visualwizardApp/index.html')

# Create your views here.
