from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    create_band,
    create_band_follow,
    create_venue,
    create_venue_follow,
    get_all_bands,
    get_all_venues,
    get_followed_bands,
    get_followed_venues,
    get_user,
    make_show_date,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("get_user/<int:user_id>/", get_user),
    path("create_band/", create_band),
    path("create_venue/", create_venue),
    path("get_all_bands/", get_all_bands),
    path("get_all_venues/", get_all_venues),
    path("follow_band/", create_band_follow),
    path("follow_venue/", create_venue_follow),
    path("get_followed_bands/<int:user_id>/", get_followed_bands),
    path("get_followed_venues/<int:user_id>/", get_followed_venues),
    path("make_show_date/", make_show_date),
]
