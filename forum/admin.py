from django.contrib import admin
from .models import Post, Profile
from django.contrib.auth.models import Group #importing just for unregistiration 


from django.contrib import admin



admin.site.site_header = "Admin Dashboard Discussion Forum"

class SnippetAdmin(admin.ModelAdmin):
    list_display = ("user1","post_id","post_content")
    #list_filter = ("user1","post_content") #lets check this after creating user access

admin.site.register(Post, SnippetAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)



