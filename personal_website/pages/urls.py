from django.urls import path
from .views import home_page_view, about_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
    # You can add more URL patterns here for other views
    path("about/", about_page_view, name="about"),
    # path('contact/', contact_page_view, name='contact'),
    # path('blog/', blog_page_view, name='blog'),
    # path('services/', services_page_view, name='services'),
    # path('portfolio/', portfolio_page_view, name='portfolio'),
    # path('testimonials/', testimonials_page_view, name='testimonials'),
    # path('faq/', faq_page_view, name='faq'),
    # path('terms/', terms_page_view, name='terms'),
    # path('privacy/', privacy_page_view, name='privacy'),
    # path('sitemap/', sitemap_page_view, name='sitemap'),
    # path('login/', login_page_view, name='login'),
    # path('register/', register_page_view, name='register'),
    # path('logout/', logout_page_view, name='logout'),
    # path('profile/', profile_page_view, name='profile'),
    # path('settings/', settings_page_view, name='settings'),
    # path('search/', search_page_view, name='search'),
    # path('news/', news_page_view, name='news'),
    # path('events/', events_page_view, name='events'),
    # path('gallery/', gallery_page_view, name='gallery'),
    # path('downloads/', downloads_page_view, name='downloads'),
    # path('help/', help_page_view, name='help'),
    # path('feedback/', feedback_page_view, name='feedback'),
    # path('careers/', careers_page_view, name='careers'),
    # path('sponsors/', sponsors_page_view, name='sponsors'),
    # path('partners/', partners_page_view, name='partners'),
    # path('press/', press_page_view, name='press'),
    # path('terms-of-service/', terms_of_service_page_view, name='terms_of_service'),
    # path('privacy-policy/', privacy_policy_page_view, name='privacy_policy'),
    # Add more URL patterns as needed
]
