from django.contrib import admin
from .models import Novel, Vol, Chapter

# Register your models here.
#
class VolInLine(admin.TabularInline):
    model = Vol
    extra = 3

class NovelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Author', {'fields': ['author'], 'classes': ['collapse']}),
    ]
    inlines = [VolInLine]

    list_display = ('title', 'author')
    search_fields = ['title']

admin.site.register(Novel, NovelAdmin)
