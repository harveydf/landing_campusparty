import json

from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView

from celery import chain

from .models import UserRegistered, Scenario
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
        scenarios = self.get_scenarios()
        context.update(dict(scenarios=scenarios))

        if self.request.GET.get('token'):
            try:
                user_registered = UserRegistered.objects.get(token=self.request.GET.get('token'))
            except UserRegistered.DoesNotExist:
                pass
            else:
                context.update(dict(name=user_registered.name))

        return context

    def get_scenarios(self):
        return Scenario.objects.all()


    def form_valid(self, form):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')

        workflow = chain(register_user.s(name=name, email=email), save_welcome_mail.s())
        workflow.delay()

        data = dict(name=name)
        return self.render_to_json_response(data)

    def form_invalid(self, form):
        return self.render_to_json_response(form.errors, status=400)


class ScenarioTemplateView(AjaxMixin, TemplateView):
    template_name = 'scenario.html'

    def get(self, request, *args, **kwargs):
        context = super(ScenarioTemplateView, self).get_context_data(**kwargs)

        try:
            scenario = Scenario.objects.get(name=kwargs['scenario'])
        except Scenario.DoesNotExits:
            data = dict(error='Scenario not found.')
            return self.render_to_json_response(data, stauts=404)

        speakers = scenario.speaker_set.all()

        if not speakers:
            return self.render_to_json_response({'error': 'Speakers not found.'}, status=400)


        context.update(dict(speakers=speakers))
        return self.render_to_response(context)
