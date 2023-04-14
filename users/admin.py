from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User

# Register your models here.


@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    inlines = (BasketAdmin, )


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created', )
