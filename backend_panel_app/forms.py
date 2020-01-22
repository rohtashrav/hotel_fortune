from django import forms
from backend_panel_app.models import RoleDetails

class RoleDetailsForm(forms.ModelForm):
    class Meta:
        model = RoleDetails
        exclude = [
            'id',
            'role_id',
            'name',
            'email',
            'password',
            'mobile',
            'address',
            'gender',
            'verifry_link',
            'otp',
            'otp_time',
            'is_active',
        ]