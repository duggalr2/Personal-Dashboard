from django.contrib import admin

# Register your models here.

from .models import Blog_post


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["name", "content", "pub_date"]
	search_fields = ["name", "content"]
	class Meta:
		model = Blog_post


admin.site.register(Blog_post, PostModelAdmin)