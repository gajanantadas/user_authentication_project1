from django.urls import path
from . import views
urlpatterns = [
    path('sign/',views.Register_view,name='sign_up'),
    path('login/',views.Login_view,name='log_in'),
    path('prof/',views.Profile_view,name='profile'),
    path('change/',views.ChangePword_view,name='change'),
    path('logout/',views.logout_view,name='log_out'),
    path('detail/<int:id>',views.Userdetail,name='userdetail')
]