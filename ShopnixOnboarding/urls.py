from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='step1/')),  # Redirect root to step1
    path('step1/', include('onboarding.urls')), 
       # Include onboarding app URLs
]