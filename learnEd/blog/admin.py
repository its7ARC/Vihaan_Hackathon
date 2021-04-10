from django.contrib import admin

# Register your models here.

from .models import Topic,Blog,Profile

class BlogInline(admin.StackedInline):           #TablularInline
	model = Blog
	extra = 5

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields':['name']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),
		
	]
	inlines = [BlogInline]

admin.site.register(Topic,TopicAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user','date_of_birth','photo']

	