from django.contrib import admin

# Register your models here.
from TestModel.models import eaxm_db, Contact, Tag

class ContactAdmin(admin.ModelAdmin):
	fields = ('name', 'email')		


class ContactAdmin2(admin.ModelAdmin):
	fieldsets = (
		['Main', {
			'fields':('name', 'email'),
		}],
		['Advance',{
			'classes':('clollapse',),
			'fields':('age',),
		}]
	)

class TagInline(admin.TabularInline):
	model = Tag


class ContactAdmin3(admin.ModelAdmin):
	list_display = ('name', 'age', 'email')
	search_fields = ('name', 'email',)
	inlines = [TagInline]
	fieldsets = (
		['Main',{
			'fields':('name','email'),
		}],
		['Advance',{
			'classes':('clollapse',),
			'fields':('age',),
		}]
	)

admin.site.register( Contact, ContactAdmin3)
admin.site.register([eaxm_db])