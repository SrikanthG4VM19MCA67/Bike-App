from django.urls import path
from . import views
from bike.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('upload/',views.upload,name='upload-bike'),
    path('update/<int:bike_id>',views.update_bike),
    path('delete/<int:bike_id>',views.delete_bike),
]

if DEBUG:
    urlpatterns+=static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)