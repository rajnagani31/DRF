from django.urls import path, include
from .views import CompanyView ,CompanyDataView
urlpatterns = [
    # POST API FOR COMPANY
    path("company/",CompanyView.as_view(),name="Company-create"),
    # GET
    path("companyGET/<int:pk>/",CompanyView.as_view(), name="company-get"),

    # PUT 
    path("companyPUT/<int:pk>/",CompanyView.as_view(),name="company-put"),
    # DELETE
    path("companyDELETE/<int:pk>/",CompanyView.as_view(),name="company_delete"),

    # API FOR COMPANY DATA
    path("companydata/", CompanyDataView.as_view(), name="companydata-create"),
    path("companydata/<int:pk>/",CompanyDataView.as_view(), name="companydata-get"),
]