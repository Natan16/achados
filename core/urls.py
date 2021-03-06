from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/google_login$', views.google_login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),
    url(r'^api/adiciona_registro', views.adiciona_registro),
    url(r'^api/lista_correspondencias$', views.lista_correspondencias),
    url(r'^api/envia_email$', views.envia_email),
    url(r'^api/exclui_registro$', views.exclui_registro),
    url(r'^api/consulta_registros$', views.consulta_registros),
    url(r'^api/toggle_status$', views.toggle_status),

]
