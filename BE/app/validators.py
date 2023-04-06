import re
from django.core.exceptions import ValidationError

def validate_username(value):
    if re.search(r'[^a-zA-Z0-9-_]', value):
        raise ValidationError('사용자 ID는 영문자, 숫자, 하이픈(-) 및 밑줄(_)만 포함해야 합니다.')
