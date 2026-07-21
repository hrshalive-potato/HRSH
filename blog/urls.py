from django.urls import path
from . import views

urlpatterns = [
    # We will add blog URLs here later!
    path('',views.post_list,name='post_list'),
    path('post/<slug:slug>',views.post_detail,name='post_details'),
]
