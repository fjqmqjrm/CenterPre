from django.shortcuts import render
from django.contrib import messages

from .forms import CustomCsUserChangeForm

def mypage_view(request):
    return render(request, "mypage/mypage.html")

def edit_view(request):
    return render(request, "mypage/info_edit.html")

def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, "mypage/mypage.html")
        else:
            print(user_change_form.errors)
            # return render(request, "mypage/mypage.html")
    else:
        user_change_form = CustomCsUserChangeForm(instance = request.user)

        return render(request, 'mypage/info_edit.html', {'user_change_form':user_change_form})
