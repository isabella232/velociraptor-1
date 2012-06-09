from django.contrib import admin
from django.contrib.auth.models import Group

from deployment import models

class ConfigValueAdmin(admin.ModelAdmin):
    model = models.ConfigValue

admin.site.register(models.ConfigValue, ConfigValueAdmin)

class ConfigIngredientInline(admin.TabularInline):
    model = models.ConfigIngredient

class ConfigRecipeAdmin(admin.ModelAdmin):
    inlines = [ConfigIngredientInline]
    search_fields = ['name', 'ingredients__label', 'ingredients__value']

class HostInline(admin.TabularInline):
    model = models.Host

class SquadAdmin(admin.ModelAdmin):
    inlines = [HostInline]

admin.site.register(models.ConfigRecipe, ConfigRecipeAdmin)

admin.site.register(models.App)
admin.site.register(models.Build)
admin.site.register(models.Release)
admin.site.register(models.Host)
admin.site.register(models.DeploymentLogEntry)
admin.site.register(models.Squad, SquadAdmin)
admin.site.register(models.Swarm)


# Unregister the Django 'group' model, as I don't think we'll be using it.
admin.site.unregister(Group)

# Unregister the djcelery models.
#import djcelery.models
#admin.site.unregister(djcelery.models.TaskState)
#admin.site.unregister(djcelery.models.WorkerState)
#admin.site.unregister(djcelery.models.IntervalSchedule)
#admin.site.unregister(djcelery.models.CrontabSchedule)
#admin.site.unregister(djcelery.models.PeriodicTask)
