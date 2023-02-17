from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
class OrganisorAndLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated and is an organisor."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect("leads:landing")
        return super().dispatch(request, *args, **kwargs)