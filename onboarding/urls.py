from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Homepage
    path('verify-otp/', views.verify_otp, name='verify_otp'),  # Verify OTP
    path('create-store/', views.create_store, name='create_store'),  # Create Store
    path('step1/', views.step1, name='step1'),  # Step 1 - Theme Selection
    path('apply-theme/', views.apply_theme, name='apply_theme'),  # Apply Theme
    path('step2/', views.step2, name='step2'),  # Step 2 - Add Product Type and Category
    path('add_product/', views.add_product, name='add_product'),
    path('setup-store/', views.setup_store, name='setup_store'),
    path('step3/', views.step3, name='step3'),

]