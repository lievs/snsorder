from django.urls import path
from snsorder.views import index, indexItem

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name="detail"),

]
