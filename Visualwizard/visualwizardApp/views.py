from django.conf import settings
from django.shortcuts import render
from django.http import request
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import os
from io import BytesIO
import base64

from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import cv2  # Optional, for advanced techniques
import numpy as np

def enhance_image(image, enhancement_type, factor=1.0):
    """
    Applies image enhancement based on the specified type and factor.

    Args:
        image: PIL Image object
        enhancement_type: String representing the type of enhancement (e.g., 'brightness', 'contrast', 'sharpness')
        factor: Float value to adjust the enhancement level

    Returns:
        Enhanced PIL Image object
    """
    # Convert PIL Image to NumPy array
    image_array = np.array(image)

    if enhancement_type == 'brightness':
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)
    elif enhancement_type == 'contrast':
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)
    elif enhancement_type == 'sharpness':
        enhancer = ImageEnhance.Sharpness(image)
        return enhancer.enhance(factor)
    elif enhancement_type == 'scale':
        # Scale the image based on the factor (e.g., double the size)
        width, height = image.size
        scaled_image = image.resize((int(width * factor), int(height * factor)))
        return scaled_image
    elif enhancement_type == 'inverse':
        # Apply inverse transform to the image
        return ImageOps.invert(image)
    elif enhancement_type == 'edge_detection':
        # Apply edge detection using Canny algorithm from OpenCV
        image_array = np.array(image)
        edges = cv2.Canny(image_array, 100, 200)
        return Image.fromarray(edges)
    elif enhancement_type == 'color_correction':
        # Apply color correction using histogram equalization from OpenCV
        image_array = np.array(image)
        corrected_image_array = cv2.equalizeHist(image_array)
        return Image.fromarray(corrected_image_array)
    elif enhancement_type == 'image_gradients':
        # Compute image gradients using Sobel filter from OpenCV
        image_array = np.array(image)
        grad_x = cv2.Sobel(image_array, cv2.CV_64F, 1, 0, ksize=5)
        grad_y = cv2.Sobel(image_array, cv2.CV_64F, 0, 1, ksize=5)
        gradient_image = cv2.magnitude(grad_x, grad_y)
        return Image.fromarray(gradient_image)
    elif enhancement_type == 'crop':
        # Crop the image based on specified factor (e.g., center crop)
        width, height = image.size
        left = (width - int(width * factor)) / 2
        top = (height - int(height * factor)) / 2
        right = (width + int(width * factor)) / 2
        bottom = (height + int(height * factor)) / 2
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image
    elif enhancement_type == 'rotate':
        # Rotate the image by the specified angle (in degrees)
        return image.rotate(factor)
    elif enhancement_type == 'blend':
        # Blend the image with a solid color (e.g., white)
        blended_image = Image.new('RGB', image.size, (255, 255, 255))
        return Image.blend(image, blended_image, factor)
    elif enhancement_type == 'thresholding':
        # Apply thresholding to binarize the image
        image_array = np.array(image)
        _, thresholded_image = cv2.threshold(image_array, 128, 255, cv2.THRESH_BINARY)
        return Image.fromarray(thresholded_image)
    elif enhancement_type == 'deblurring':
        # Deblur the image using Gaussian blur from OpenCV
        image_array = np.array(image)
        deblurred_image_array = cv2.GaussianBlur(image_array, (5, 5), 0)
        return Image.fromarray(deblurred_image_array)
    elif enhancement_type == 'noise_reduction':  # Using OpenCV (optional)
        gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        denoised_image_array = cv2.fastNlMeansDenoising(gray_image)
        # Convert NumPy array back to PIL Image
        return Image.fromarray(denoised_image_array)
    else:
        raise ValueError(f"Invalid enhancement type: {enhancement_type}")

def index(request):
    if request.method == 'POST':
        if 'original_image' not in request.FILES:
            return HttpResponseBadRequest('No image uploaded.')

        original_image = request.FILES['original_image']
        try:
            image = Image.open(original_image)

            # Get enhancement type and factor from request data
            enhancement_type = request.POST.get('enhancement_type')
            factor = float(request.POST.get('factor', 1.0))

            enhanced_image = enhance_image(image.copy(), enhancement_type, factor)

            original_image_io = BytesIO()
            image.save(original_image_io, format='JPEG')
            original_image_data = original_image_io.getvalue()
            original_image_base64 = base64.b64encode(original_image_data).decode('utf-8')

            enhanced_image_io = BytesIO()
            enhanced_image.save(enhanced_image_io, format='JPEG')
            enhanced_image_data = enhanced_image_io.getvalue()

            original_image_url = f'data:image/jpeg;base64,{original_image_base64}'

            return JsonResponse({'original_image_url': original_image_url, 'enhanced_image': enhanced_image_data.decode('latin-1')})

            # Optionally, save enhanced image to media directory
            #enhanced_image_filename = f'{original_image.name.split(".")[0]}_{enhancement_type}_enhanced.jpg'
            #enhanced_image_path = os.path.join(settings.MEDIA_ROOT, 'enhanced', enhanced_image_filename)
            #enhanced_image.save(enhanced_image_path)

            #enhanced_image_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, 'enhanced', enhanced_image_filename))

        except (IOError, ValueError, TypeError) as e:
            return HttpResponseBadRequest(f'Error processing image: {e}')

        #context = {
            #'original_image_url': original_image_url,
            #'enhanced_image_url': os.path.join(settings.MEDIA_ROOT, 'enhanced', enhanced_image_filename),
            #'enhanced_image_url' : enhanced_image_url

        #}
        #return render(request, 'visualwizardApp/index.html', context)

    else:
        return render(request, 'visualwizardApp/index.html')

def chatbot(request):
    if request.method == 'POST':
        enhancement_type = request.POST.get('enhancement_type')
        factor = float(request.POST.get('factor', 1.0))
        original_image = request.FILES.get('original_image')

        try:
            image = Image.open(original_image)
            enhanced_image = enhance_image(image, enhancement_type, factor)
            enhanced_image_io = BytesIO()
            enhanced_image.save(enhanced_image_io, format='JPEG')
            enhanced_image_data = enhanced_image_io.getvalue()

            original_image_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, 'originals', original_image.name))
            # You can also save the enhanced image to a file if needed

            return JsonResponse({'original_image_url': original_image_url,'enhanced_image': base64.b64encode(enhanced_image_data).decode('utf-8')})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})
