from django.shortcuts import redirect, render
from .models import Topic, Choice
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def index(request):

    t = Topic.objects.all()
    context = {
        "tlist" : t,
    }
    return render(request, "vote/index.html", context)


def create(request):
    if request.method == "POST":
        sub = request.POST.get("subject")
        if sub:
            wri = request.user.username
            con = request.POST.get("content")
            pub = timezone.now()
            t = Topic(subject=sub, writer=wri, content=con, pubdate=pub)
            names = request.POST.getlist("name")
            pics = request.FILES.getlist("pic")
            if len(names) > 1 and len(pics) > 1:
                comments = request.POST.getlist("comment")
                t.save()
                for name, pic, comment in zip(names, pics, comments):
                    Choice(subject=t, name=name, pic=pic, comment=comment).save()
                return redirect("vote:index")
    return render(request, "vote/create.html")



def cancel(request, tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.remove(request.user)
    clist = t.choice_set.all()
    for i in clist:
        if request.user in i.choicer.all():
            i.choicer.remove(request.user)
    return redirect("vote:detail", tpk=tpk)



def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    t.voter.add(request.user)
    cpk = request.POST.get("choice")
    c = Choice.objects.get(id=cpk)
    c.choicer.add(request.user)
    return redirect("vote:detail", tpk=tpk)


def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "to" : t,
        "clist" : c,
    }
    return render(request, "vote/detail.html", context)



