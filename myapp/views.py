from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.: 어떤 데이터가 어떻게 처리될 지 알려주는 함수! model과 templates를 연결.
def main(request):
    post_list = Post.objects.all() 
    return render(request, 'main.html', {'post_list':post_list})

    #쿼리셋과 메소드의 형식: "모델.쿼리셋(Object).메소드"
    #all():포스트로 만든 모든 쿼리셋 객체들을 불러오라는 소리
        #.count: 개수 반환
        # .first(): 첫번째 객체 반환
        # .last(): 마지막 객체 반환
    #쿼리셋:포스트 안에 있는 객체를 담아준다.모델로부터 객체의 목록을 전달받을 수 있음.=.object
    #쿼리셋을 이용해서 받은 데이터를 정렬, 표시하는 방법을 메소드라고 함.

def detail(request, post_id):
    post=Post.objects.get(id=post_id)
    comments = post.comment_set.all().order_by('-pub_date')
    return render(request,"detail.html", {'post':post, 'comments': comments})

def create(request):
    if request.method=="POST":
        post=Post()
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('main')

    else:
        return render(request, 'create.html')

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    # 각 글의 고유한 아이디를()에 넣어야함, id=는 변수, post_id=상수값. 
    post.delete()
    return redirect('main')

#어려운 부분: 갱신하기
def edit(request,post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('')       

    else:
        post=Post.objects.get(id=post_id)
        return render (request, 'edit.html',{"post": post})

def comment_create(request, post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        comment=Comment(post=post)
        # 파랑포스트는 models에 있는 변수 post, 흰 포스트는 객체의 값 특정된 것(엄마=엄마이름)
        comment.content=request.POST['content']
        comment.save()
        
        return redirect('detail',post_id)

def result(request):
        text= request.GET['fulltext']
        words=text.split()
        # 텍스트를 공백기준으로 나눠 스트링으로 만들어줌
        word_dic = {}

        for word in words:
                if word in word_dic:
                # increase
                         word_dic[word]+=1
                else:
                        # add to dic
                        word_dic[word]=1

        return render(request, 'result.html', {'full': text, 'total':len(words), 'dic': word_dic.items()})

# len(words)=원문을 공백 기준으로 나눴을 때 생긴 단어들을 리스트에 넣은 뒤, 리스트의 길이를 세면 총 단어수!

def more(request, post_id):
    post_more = get_object_or_404(Post, pk = post_id ) #post_id번째 블로그 객체

    return render(request, 'more.html',{'post': post_more})