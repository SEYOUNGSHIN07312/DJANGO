from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # settings.py의 AUTH_USER_MODEL에서 가져옴
        model = get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        # settings.py의 AUTH_USER_MODEL에서 가져옴
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')