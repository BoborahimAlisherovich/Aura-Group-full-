from django.urls import path
from .views import (
    IndexView,
    AboutView,
    ServicesView,
    CareerView,
    career_detail_view,
    service_request_view,
    PortfolioView,
    PortfolioDetailsView,
    contact_view,
    like_project_view,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<int:pk>/', service_request_view, name='service_request'),
    path('career/', CareerView.as_view(), name='career'),
    path('career/<int:pk>/', career_detail_view, name='career_detail'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', PortfolioDetailsView.as_view(), name='portfolio_detail'),
    path('portfolio/<int:pk>/like/', like_project_view, name='like_project'),
    path('contact/', contact_view, name='contact'),
]
