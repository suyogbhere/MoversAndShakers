from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('logout/',views.Logout,name='logout'),
    path('add_service/',views.add_service,name='add_service'),
    path('manage_service/',views.manage_service,name='manage_service'),
    path('edit_service/<int:pk>',views.edit_service,name='edit_service'),
    path('delete_service/<int:pk>',views.delete_service,name='delete_service'),
    path('show_services/',views.show_services,name='show_services'),
    path('about/',views.about,name='about'),
    path('request_quote/',views.request_quote,name='request_quote'),
    path('new_booking/',views.new_booking,name='new_booking'),
    path('view_bookingdetail/<int:pk>',views.view_bookingdetail,name='view_bookingdetail'),
    path('old_booking/',views.old_booking,name='old_booking'),
    path('delete_booking/<int:pk>',views.delete_booking,name='delete_booking'),
    path('contact/',views.contact,name='contact'),
    path('unread_queries/',views.unread_queries,name='unread_queries'),
    path('read_queries/',views.read_queries,name='read_queries'),
    path('view_queries/<int:pk>',views.view_queries,name='view_queries'),
    path('delete_queries/<int:pk>',views.delete_queries,name='delete_queries'),
    path('search',views.search,name='search'),
    path('betweendate_bookingreport',views.betweendate_bookingreport,name='betweendate_bookingreport'),
    path('betweendate_queryreport',views.betweendate_queryreport,name='betweendate_queryreport'),
    path('change_password',views.change_password,name='change_password'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)