from django.contrib import admin
from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('email', 'name', 'password', 'id', 'created', 'modified')


admin.site.register(Member, MemberAdmin)