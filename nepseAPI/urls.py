from django.urls import path, include
from .views import *


urlpatterns = [
    path('companies/', CompanyListedView.as_view() ),
    path('live-trade/',liveTradeView.as_view())

]
