from django.shortcuts import render, redirect, reverse
from ..login.models import User
from models import T_plan


def index(request):
	user = User.objects.get(id=request.session['user_id'])
	
	context = {
		'user': user,
		'others': T_plan.objects.all(),
		'favs': T_plan.objects.filter(joined_by=user).all(),
	}	
	print context['favs']
	return render(request, 'main_app/index.html', context)

# 'favs': User.objects.filter(joined_by__in=user).all(),
# 'allmsgs': User.objects.get(id = number).messages.all(),

def logout(request):
	del request.session['user_id']
	return redirect('/')

def makeplans(request):
	
	return render(request, 'main_app/makeplans.html')

def success(request, number):
	plan = T_plan.objects.get(id = number)
	content = {
		'plan': plan,
		'alljoins': User.objects.filter(joinedplans = plan),
	}
	print content['alljoins']
	return render(request, 'main_app/success.html', content)

def join(request):

	print 'favorite!!!!!!'
	joiner = User.objects.get(id = request.session['user_id'])	
	plan_id = request.POST['plan_id']
	newplan = T_plan.objects.get(id = plan_id)
	newplan.joined_by.add(joiner)
	print newplan.joined_by
	
	return redirect(reverse('dashboard'))

def plans(request):
	print 'COOOOL Plans!!!!'
	user = User.objects.get(id = request.session['user_id'])
	destination = request.POST['destination']
	description = request.POST['description']
	startdate = request.POST['startdate']
	enddate = request.POST['enddate']
	new_plan = T_plan.objects.create(destination=destination, user=user, description=description, startdate=startdate, enddate=enddate)
	print new_plan	
	return redirect(reverse('dashboard'))


	# <h3>My Plans!</h3>
	# {% for each in favs %}
	# {{ each.destination }}||<a href="/main_app/success/{{each.user.id}}">{{ each.user.first_name }}</a>
	# <form action="{% url 'unfavorite' %}" method="POST">
	# 	{% csrf_token %}
	# 	<input type="hidden" name="unfav" value="{{each.id}}">
	# 	<input type="submit" value="Ok!"></input>	
	# </form>
	# {% endfor %}


	

