from .models import *

def get_profpic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.profileimg
        return{'picture':pic}

    return {}
