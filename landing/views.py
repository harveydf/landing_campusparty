from django.views.generic import CreateView

from .models import UserRegistered
from .forms import LandingForm
from .tasks import register_user


class LandingCreateView(CreateView):
    model = UserRegistered
    form_class = LandingForm
    template_name = 'landing.html'

    # def form_valid(self, form):
    #     register_user.delay(name=)
