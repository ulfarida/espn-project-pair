from django.contrib import admin
from .models import Berita, Detail, Team, Match
from django import forms
# Register your models here.

class TeamModelForm( forms.ModelForm ):
    team_image = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Team
        fields = '__all__'
 
class TeamAdmin( admin.ModelAdmin ):
    form = TeamModelForm

admin.site.register(Berita)
admin.site.register(Detail)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match)

