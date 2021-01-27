from django.shortcuts import render,redirect
from .models import user
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request,'index.html')


def main(request):

	user1=user.objects.all()

	if request.method == 'POST' :
		val1=request.POST['gmail']
		val2=request.POST['password']
		for i in user1:
			if i.gmail==val1 and i.password==val2 :
				return render(request,'main.html',{'userr':i,'persons':user1})

		messages.info(request,'invalid credential')
		return redirect('index')


		'''user1=user.objects.all()
	if request.method=='POST':
		gmail1=request.POST['gmail']
		password1=request.POST['password']
		print(gmail1)
		print(password1)
		x=auth.authenticate(gmail='vigneshdask@gmail.com' , password='1111')
		print(x)
		if x is None:
			return render(request,'index.html')
		else:
			return render(request,'main.html',{'persons':user1})'''

def forgot(request):
	return render(request,'forgot.html')

def new(request):
	return render(request,'new.html')
