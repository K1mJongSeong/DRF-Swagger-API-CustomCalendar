from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_password_length(password, **kwargs):
    """
    Validate whether the password is at least 4 characters long.
    """
    if len(password) < 4:
        raise ValidationError(
            _("비밀번호는 최소 4자 이상이어야 합니다."),
            code='password_too_short',
            params={'min_length': 4},
        )
