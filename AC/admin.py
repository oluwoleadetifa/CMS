from django.apps import apps
from django.contrib import admin
from portal.models import User

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
