from django.conf.urls import url,include
from sub import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^cust/$',views.cust,name="cust"),
    url(r'^sact/$',views.sact,name="sact"),
    url(r'^calc/$',views.calc,name="calc"),
    url(r'^Add/$',views.Add,name="Add"),
    url(r'^table/$',views.table,name="table"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)