import json

from django.http import HttpResponse
from django.views.generic import CreateView

from celery import chain

from .models import UserRegistered
from .forms import LandingForm
from .tasks import register_user, save_welcome_mail


class AjaxMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)


class LandingCreateView(AjaxMixin, CreateView):
    model = UserRegistered
    form_class = LandingForm
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingCreateView, self).get_context_data(**kwargs)

        if self.request.GET.get('token'):
            try:
                user_registered = UserRegistered.objects.get(token=self.request.GET.get('token'))
            except UserRegistered.DoesNotExist:
                pass
            else:
                context.update(dict(name=user_registered.name))

        return context


    def form_valid(self, form):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')

        workflow = chain(register_user.s(name=name, email=email), save_welcome_mail.s())
        workflow.delay()

        data = dict(name=name)
        return self.render_to_json_response(data)

    def form_invalid(self, form):
        return self.render_to_json_response(form.errors, status=400)


