"""trail_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workflow.program_workflow import (programRouter,
                                       programSingleRouter,
                                       programSdgRouter)
from workflow.sdg_workflow import sdgRouter, singleSdgRouter, sdgIndicatorsRouter, singleSdgIndicatorRouter
# from workflow.imageUpload_workflow import imageUploadURLRouter

urlpatterns = [
    path('admin/', admin.site.urls),

    path('programs/', programRouter, name="program-router"),

    path('programs/<int:programId>/', programSingleRouter,
         name="program-single-router"),

    path('programs/<int:programId>/sdgs',
         programSdgRouter, name="program-sdg-router"),

    path('sdgs/', sdgRouter, name="sdg-router"),

    path('sdgs/<int:sdgId>/', singleSdgRouter, name='single-sdg-router'),

    path('indicators/', sdgIndicatorsRouter, name="sdg-indicators-router"),

    path('indicators/<int:indicatorId>/', singleSdgIndicatorRouter,
         name='single-sdgIndicator-router')
    # path('images/', imageUploadURLRouter, name="imageUploadURL-Router"),
]
