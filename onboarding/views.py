from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from . import models
from .models import Order, Product #Add all the models you are using.
from django.utils import timezone

from .models import *

def welcome(request):
    return render(request, 'onboarding/welcome.html')

def create_store(request):
    return render(request, 'onboarding/create_store.html')


def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')  # Get the OTP entered by the user
        # Add your OTP verification logic here (e.g., check if OTP is valid)
        if otp == "444331":  # Replace with your actual OTP verification logic
            return redirect('step1')  # Redirect to Step 1 if OTP is valid
        else:
            # If OTP is invalid, show an error message
            return render(request, 'onboarding/create_store.html', {'error': 'Invalid OTP'})
    return redirect('create_store')  # Redirect back to the Create Store page if the request is not POST


def step1(request):
    return render(request, 'onboarding/step1.html')

def apply_theme(request):
    if request.method == 'POST':
        selected_theme = request.POST.get('theme')  # Get the selected theme
        # Save the selected theme to the session or database
        request.session['selected_theme'] = selected_theme
        return redirect('step2')  # Redirect to Step 2 after applying the theme
    return redirect('step1')  


def step2(request):
    if request.method == 'POST':
        return redirect('step3')
    return render(request, 'onboarding/step2.html')




def add_product(request):
    net_amount = 0
    image_url = None

    if request.method == 'POST':
        # Handle image upload
        product_image = request.FILES.get('productImage')
        if product_image:
            file_name = default_storage.save(product_image.name, product_image)
            image_url = default_storage.url(file_name)

        # Process form data
        price = float(request.POST.get('price', 0))
        discount = float(request.POST.get('discount', 0))
        gst = float(request.POST.get('gst', 0))
        delivery_charge = float(request.POST.get('deliveryCharge', 0))
        stock = int(request.POST.get('stock', 0))

        # Calculate net amount
        discount_amount = (price * discount) / 100
        price_after_discount = price - discount_amount
        gst_amount = (price_after_discount * gst) / 100
        net_amount = price_after_discount + gst_amount + delivery_charge

    # Pass data to the template
    context = {
        'image_url': image_url,
        'net_amount': net_amount,
    }
    return render(request, 'onboarding/add_product.html', context)


def setup_store(request):
    return render(request, 'onboarding/setup_store.html')


  # Assuming you have a PricingPlan model





def step3(request):
    
    return render(request, 'onboarding/step3.html')