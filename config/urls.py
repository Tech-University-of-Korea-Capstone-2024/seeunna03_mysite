from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
from common import views as common_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common_views.home, name='home'),  # 루트 URL → 홈화면
    
    
    path('team/', include('team.urls')),
    path('match/', include('match.urls')),
    path('pybo/', include('pybo.urls')),       # 기존 게시판 URL은 /pybo/ 로 진입
    
    path('common/', include('common.urls')),   # 로그인/회원가입 등
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)