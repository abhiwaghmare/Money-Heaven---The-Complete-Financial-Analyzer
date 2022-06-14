
from django.contrib import admin
from django.urls import path,include
from insurance import views
from django.contrib.auth.views import LogoutView,LoginView
from HomeApp.views import home,news,ulogout
from insurance.views import home_view
from pred_app.views import redirect_root, search,pred
from crypto_app.views import redirect_root, searchCrypt,predCrypt
from loanApp.views import loanhome,loanpredict
from customer.views import customerclick_view,customer_signup_view,customer_dashboard_view,apply_policy_view,apply_view,history_view,ask_question_view,question_history_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('insuranceHome/',home_view,name='insuranceHome'),
    path('', redirect_root),
    path('pred_app/',include('pred_app.urls')),
    path('crypto_app/',include('crypto_app.urls')),
    path('cryptPred/',pred,name='cryptPred'),
    path('search/<str:se>/<str:stock_symbol>/', search, name='predict_stock'),
    path('searchCrypt/<str:se>/<str:stock_symbol>/',searchCrypt,name='predict_crypt'),
    path('loanhome/',loanhome,name='loanhome'),
    path('loanpredict/',loanpredict,name='loanpredict'),
    path('news/',news,name='news'),

    path('customer/customerclick',customerclick_view,name='customerclick'),
    path('customer/customersignup',customer_signup_view,name='customersignup'),
    path('customer/customer-dashboard',customer_dashboard_view,name='customer-dashboard'),
    path('customer/customerlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='customerlogin'),

    path('apply-policy',apply_policy_view,name='apply-policy'),
    path('apply/<int:pk>',apply_view,name='apply'),
    path('history',history_view,name='history'),

    path('ask-question',ask_question_view,name='ask-question'),
    path('question-history',question_history_view,name='question-history'),
# LogoutView.as_view(template_name='insurance/logout.html')
    path('ulogout',ulogout,name='ulogout'),
    path('logout',views.logout,name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    
    path('insuranceHome/adminlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('admin-policy', views.admin_policy_view,name='admin-policy'),
    path('admin-add-policy', views.admin_add_policy_view,name='admin-add-policy'),
    path('admin-view-policy', views.admin_view_policy_view,name='admin-view-policy'),
    path('admin-update-policy', views.admin_update_policy_view,name='admin-update-policy'),
    path('update-policy/<int:pk>', views.update_policy_view,name='update-policy'),
    path('admin-delete-policy', views.admin_delete_policy_view,name='admin-delete-policy'),
    path('delete-policy/<int:pk>', views.delete_policy_view,name='delete-policy'),

    path('admin-view-policy-holder', views.admin_view_policy_holder_view,name='admin-view-policy-holder'),
    path('admin-view-approved-policy-holder', views.admin_view_approved_policy_holder_view,name='admin-view-approved-policy-holder'),
    path('admin-view-disapproved-policy-holder', views.admin_view_disapproved_policy_holder_view,name='admin-view-disapproved-policy-holder'),
    path('admin-view-waiting-policy-holder', views.admin_view_waiting_policy_holder_view,name='admin-view-waiting-policy-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),
]
