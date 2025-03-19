from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pybo.models import Question, Answer  # 작성한 질문/답변 조회 용

def home(request):
    """사이트 메인(홈) 페이지"""
    return render(request, 'common/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST": # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # form.cleaned_data.get은 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수
            # 이 경우 폼의 입력값은 인증시 사용할 사용자명과 비밀번호
            
            # 신규 사용자를 생성한 후에 자동 로그인
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else: # GET 요청인 경우에는 회원가입 화면을 보여준다
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

@login_required
def profile(request):
    """
    로그인한 사용자 본인의 프로필(마이페이지).
    닉네임, 이메일, 가입일, 작성 질문/답변 등 표시
    """
    user = request.user  # 현재 로그인한 User 객체
    # 작성한 질문 목록
    question_list = Question.objects.filter(author=user).order_by('-create_date')
    # 작성한 답변 목록
    answer_list = Answer.objects.filter(author=user).order_by('-create_date')

    context = {
        'user': user,
        'question_list': question_list,
        'answer_list': answer_list,
    }
    return render(request, 'common/profile.html', context)

