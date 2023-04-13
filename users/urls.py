from django.urls import path
from users.views import login, registration, profile_page_view, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile_page_view, name='profile'),
    path('logout/', logout, name='logout')
]