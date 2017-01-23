from django.shortcuts import render


def index(request):
	return render(request, 'personal/home.html')
# Create your views here.

def contact(request):
	return render(request, 'personal/basic.html', {
		'contacts':[
		'If you would like to contact me, please email me',
		'test@gmail.com',
		]
		})