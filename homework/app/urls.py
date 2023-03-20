
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('addwork/',views.add),
    path('update/<int:id>',views.update,name='update'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('first/',views.first),
    path('second/',views.second),
    path('third/',views.third),
    path('fourth/',views.fourth),
    path('fifth/',views.fifth),
    path('sixth/',views.sixth),
    path('seventh/',views.seventh),
    path('eighth/',views.eighth),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

