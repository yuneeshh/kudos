from django.contrib import admin
from core.models import Organization, OrganizationMembership, Kudos
# Register your models here.

admin.site.register(Kudos)
admin.site.register(OrganizationMembership)
admin.site.register(Organization)
