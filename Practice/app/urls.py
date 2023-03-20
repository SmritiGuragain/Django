from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('add/',views.add),
    path('describe/<int:id>',views.describe),
    path('certificate/',views.certificate),
    path('cat/',views.cat),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)