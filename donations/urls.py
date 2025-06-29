from django.urls import path
from donations import views


urlpatterns = [
    path('',views.home_page, name='home'),
    path('about/',views.about_page, name='about'),
    path('campaign/',views.campaign_page, name='campaign'),
    path('register/',views.register_page, name='register'),
    path('donate/',views.donate_page, name='donate'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('make_donation/',views.make_donation,name='make_donation'),
    path('donation_success/',views.donation_success, name='donation_success'),
    path('contact/',views.contact_page, name='contact'),
    path('contact_success/',views.contact_success, name='contact_success'),
]
