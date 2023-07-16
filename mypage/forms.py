from django.contrib.auth.forms import UserChangeForm
from users.models import User

class CustomCsUserChangeForm(UserChangeForm):
    class Meta:
        model = User()
        fields = ['username', 'email']