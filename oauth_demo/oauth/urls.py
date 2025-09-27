from django.urls import path
from .views import (
    UserApplicationList,
    UserApplicationDetail,
    UserApplicationRegistration,
    UserApplicationDelete,
    UserApplicationUpdate,
    UserAuthorizedTokenList,
    UserAuthorizedTokenDelete
)

urlpatterns = [
    path("applications/", UserApplicationList.as_view(), name="application-list"),
    path("applications/register/", UserApplicationRegistration.as_view(), name="application-register"),
    path("applications/<int:pk>/", UserApplicationDetail.as_view(), name="application-detail"),
    path("applications/<int:pk>/update/", UserApplicationUpdate.as_view(), name="application-update"),
    path("applications/<int:pk>/delete/", UserApplicationDelete.as_view(), name="application-delete"),
    
    # Token management
    path("tokens/", UserAuthorizedTokenList.as_view(), name="authorized-tokens-list"),
    path("tokens/<int:pk>/delete/", UserAuthorizedTokenDelete.as_view(), name="authorized-token-delete"),
]
