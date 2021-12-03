from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        text1 = request.POST.get("before")
        fr = request.POST.get("from")
        to = request.POST.get("to")
        translator = Translator()
        trans1 = translator.translate(text1, src=fr, dest=to)
        context.update({
            "atext" : trans1.text,
            "btext" : text1,
            "from" : fr,
            "to" : to
        }) 
    return render(request, "trans/index.html", context)