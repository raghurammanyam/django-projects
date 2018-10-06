from django.contrib import admin
from django.urls import path,include
from billpay.controllers.createuser import addUsers
from billpay.controllers.transaction import addtransaction
from billpay.controllers.payments import addpayment,updatebill
urlpatterns = [
      path('createuser',addUsers.as_view()),
      path('addbill',addtransaction.as_view()),
      path('pay',addpayment.as_view()),
      path('userbill',updatebill.as_view()),

]
