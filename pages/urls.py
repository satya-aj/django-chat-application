from django.urls import path
from .views import *

app_name = "pages"

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path("profile/<int:profile_id>", profile, name="profile"),
    path("edit/", edit_profile, name="edit"),
    path("search/", search_profile, name="search"),
    path("request/send/<int:to_profile_id>", send_request, name="send_request"),
    path("request/cancle/<int:to_profile_id>", cancle_request, name="cancle_request"),
    path("request/accept/<int:from_profile_id>", accept_request, name="accept_request"),
    path("request/delete/<int:from_profile_id>", delete_request, name="delete_request"),
    path("unfriend/<int:profile_id>", unfriend, name="unfriend"),
]