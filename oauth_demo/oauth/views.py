from oauth2_provider.views import (
    ApplicationList,
    ApplicationDetail,
    ApplicationRegistration,
    ApplicationUpdate,
    ApplicationDelete
)

from oauth2_provider.views import AuthorizedTokensListView, AuthorizedTokenDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class UserApplicationMixin(LoginRequiredMixin):
    """ Custom mixing to allow only owner access """
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_objects() if hasattr(self, 'get_object') else None
        if obj and obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UserAuthorizedTokenList(UserApplicationMixin, AuthorizedTokensListView):
    pass

class UserAuthorizedTokenDelete(UserApplicationMixin, AuthorizedTokenDeleteView):
    pass

class UserApplicationList(UserApplicationMixin, ApplicationList):
    pass

class UserApplicationDetail(UserApplicationMixin, ApplicationDetail):
    pass

class UserApplicationRegistration(UserApplicationMixin, ApplicationRegistration):
    pass

class UserApplicationUpdate(UserApplicationMixin, ApplicationUpdate):
    pass

class UserApplicationDelete(UserApplicationMixin, ApplicationDelete):
    pass
