from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

@receiver(user_logged_out)
def backup_session(sender, request, user, **kwargs):
    # 여기에서 세션 데이터를 백업하거나 처리하십시오.
    # 예를 들어, 세션에서 원하는 값을 복사해 두십시오.
    session_dict = request.session.get("session_dict", {})

    # 세션을 다시 설정하고 복사해 둔 값을 다시 저장합니다.
    request.session["session_dict"] = session_dict
