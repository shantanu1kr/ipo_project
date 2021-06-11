# this is urls.py for all pages
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('pdf/', views.addPDF, name='addpdf'),
    path('', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('summary/', views.summary, name='summary'),
    path('company-search/', views.company_search, name='company_search'),

    path('addcompany/', views.addcompany, name='addcompany'),
    path('addcompany-update/<int:company_id>/<int:tid>',
         views.addcompany_updateView, name='addcompany_update_view'),
    path('addcompany-update', views.addcompany_update, name='addcompany_update'),


    path('addcompany-2/', views.addcompany_2, name='addcompany-2'),
    path('addcompany-2-update', views.addcompany2_update, name='addcompany2update'),
    path('addcompany-2-update/<int:company_id>',
         views.addcompany_2_updateView, name='addcompany_update_view_2'),
    path('addcompany-2-extrafield/<int:company_id>',
         views.addcompany_2_extraField, name='addcompany_2_extraField'),
    path('addcompany-3/', views.addcompany_3, name='addcompany-3'),
    path('addcompany-3-update/<int:company_id>/<int:tid>',
         views.addcompany_3_updateView, name='addcompany_update_view_3'),

    path('addcompany-4/', views.addcompany_4, name='addcompany-4'),
    path('addcompany-4-update/<int:company_id>/<int:tid>',
         views.addcompany_4_updateView, name='addcompany_update_view_4'),

    path('addcompany-5/', views.addcompany_5, name='addcompany-5'),
    path('addcompany-5-update/<int:company_id>/<int:tid>',
         views.addcompany_5_updateView, name='addcompany_update_view_5'),

    path('addcompany-view/<int:company>',
         views.addcompany_view_byID, name='addcompany_view_byID'),
    path('addcompany-view/', views.addcompany_view, name='addcompany_view'),
    path('quality-view/', views.quality_view, name='quality_view'),
    path('company-detail/', views.company_details, name='quality'),
    path('ipo-search/', views.ipo_search, name='ipo-search'),
    path('addfundparty/', views.addfundparty, name='addfundparty'),
    path('review/', views.review, name='review'),

    path('add-offering/', views.add_offering, name='add_offering'),
    path('add-offershare/', views.add_offering_shares, name='add_offering_shares'),
    path('add-financial/', views.add_offering_financial,
         name='add_offering_financial'),

    # path('view-report/',views.view_report,name='view_report'),
    # path('company-details/',views.company_details,name='company_details'),
    path('company-submit-form/', views.company_submit_form,
         name='company_submit_form'),
    path('fundparty-submit-form/', views.fundparty_submit_form,
         name='fundparty_submit_form'),
    path('offering-details-submit-form/', views.offering_details_submit_form,
         name='offering_details_submit_form'),
    path('offering-shares-submit-form/', views.offering_shares_submit_form,
         name='offering_shares_submit_form'),
    path('financial-submit-form/', views.financial_submit_form,
         name='financial_submit_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
