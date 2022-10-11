from django.db.models import Q, Count
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            return redirect('eithers:detail', question.pk)
    else:
        question_form = QuestionForm()
    context = {
        'question_form': question_form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, question_pk):
    # 계산이 필요한 값 : 좌를 선택한 댓글 갯수, 우를 선택한 댓글의 갯수.
    # annotate를 써야 한다.
    count_a = Count('comment', filter=Q(comment__pick=False)) # 좌카운트
    count_b = Count('comment', filter=Q(comment__pick=True)) # 우카운트
    total_count = Count('comment') # 전체 카운트

    question = Question.objects.annotate(
        count_a=count_a, # 좌댓글 몇갠지
        count_b=count_b, # 우댓글 몇갠지
        total_count=total_count, # 댓글이 총 몇개인지 추가
    ).get(pk=question_pk) # pk에 맞는
    # 일반적인 .get 문에 2개의 pk가 추가되는 것이다. 질문을 가져오면서, 질문에 달린 댓글을 왼쪽 카운트, 오른쪽 카운트
    question.count_a # a를 선택한 댓글 갯수
    question.count_b # b를 선택한 댓글 갯수
    if question.total_count == 0: # 비율 계산하기
        a_per = 0
        b_per = 0
    else:
        a_per = round(question.count_a / question.total_count * 100)
        b_per = round(question.count_b / question.total_count * 100)

    context = {
        'question': question,
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per,
        'b_per': b_per,
    }
    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question_id = question_pk
        comment.save()
    return redirect('eithers:detail', question_pk)


def random(request):
    pass
    
    context = {
        'question': question, 
        'comments': comments,
        'comment_form': comment_form,
        'a_per': a_per, 
        'b_per': b_per,
    }

    return render(request, 'eithers/detail.html', context)
