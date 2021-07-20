import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.generic.base import View



class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        file = request.FILES
        print("file: ", file)
        with open('a.txt', 'w', encoding='utf-8') as f:
            f.write("nihao")

        return HttpResponse("success")


class CheckFile(View):

    def post(self, request):
        data = request.POST
        md5 = data.get("md5Post", None)
        print(md5)
        if md5 == "25e46b405ecca9525aae92b0217c61a9" or md5 == "8fd0845f977e2dd8259e1d0304f40d5b":
            return HttpResponse(json.dumps({"state": 1}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"state": 0}), content_type="application/json")

