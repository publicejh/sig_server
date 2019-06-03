from django.contrib import admin
from .models import Sig, SigParticipate, SigInvitationToken


class SigAdmin(admin.ModelAdmin):
    model = Sig


class SigParticipateAdmin(admin.ModelAdmin):
    model = SigParticipate


class SigInvitationTokenAdmin(admin.ModelAdmin):
    model = SigInvitationToken


admin.site.register(Sig, SigAdmin)
admin.site.register(SigParticipate, SigParticipateAdmin)
admin.site.register(SigInvitationToken, SigInvitationTokenAdmin)
