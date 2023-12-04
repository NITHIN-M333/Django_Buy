from django.shortcuts import render


# Create your views here.
def Home(request):
     return render(request,"home.html")

def list(request):
     Movies ={
          "data":[{
               "name":"panjavarna thatha",
               "year":2019,
               "summary": "Story of a innocent pet lover",
               "success":True
          },
          {
               "name":"Doctor Inncocent anu",
               "year":2007,
               "success":False
          },
          {
               "name":"aadu thomma",
               "year":1997,
               "summary":"A story of school boy become rebel after",
               "success":True
          },
          {
               "name":"napoleon",
               "year":2023,
               "summary": "There is nothing we can do",
               "success":True
          }]
     }
     return render(request,"list.html",Movies)