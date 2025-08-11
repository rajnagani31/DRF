from django.urls import path, include
from .views import CompanyView,CompanyDataView
urlpatterns = [
    path("company/",CompanyView.as_view(), name="company-create"),
    path("companyGET/<int:pk>/",CompanyView.as_view(), name="company-get"),

    # POST API FOR COMPANY DATA
    path("companydata/", CompanyDataView.as_view(), name="companydata-create"),

    # GET API FOR COMPANY DATA
    path("companydataGET/<int:pk>/",CompanyDataView.as_view(), name="companydata-get"),
    
    # PUT API FOR COMPANY DATA
    path("companydataPUT/<int:pk>/",CompanyDataView.as_view(),name = "companydata-put")
]