from django.contrib import admin
from twitter_users.models import User
from django.contrib.auth.forms import UserCreationForm


# User = settings.AUTH_USER_MODEL
class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
        ]
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = RegForm
    pass
