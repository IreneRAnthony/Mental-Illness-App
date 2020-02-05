from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/index.html')

def process_registration(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        request.POST['confirm_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.create(name = name, email = email, password = pw_hash, coin_amount = 0)
            return redirect('/registration/success')

def registration_success(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/success.html')

def process_login(request):
    if request.method == "POST":
        print("INSIDE LOGIN")
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect('/homepage')
        return redirect('/')

def logout(request):
    del request.session['userid']
    return redirect('/')

def homepage(request):
    if request.method == "GET":
        context = {
            'current_user': User.objects.get(id = request.session['userid']),
            'user_goals': Goal.objects.filter(user_id = request.session['userid']),
        }
        return render(request, 'mental_illness_app/user_homepage.html', context)

def edit_account(request):
    if request.method == "GET":
        context = {
            'current_user': User.objects.get(id = request.session['userid']),
        }
        return render(request, 'mental_illness_app/edit_account.html', context)

def update_account(request):
    if request.method == "POST":
        update = User.objects.get(id = request.session['userid'])
        update.name = request.POST['name']
        # Need to salt password after updating it!
        update.password = request.POST['password']
        update.email = request.POST['email']
        pw_hash = bcrypt.hashpw(update.password.encode(), bcrypt.gensalt())
        update.password = pw_hash
        update.save()
        return redirect('/homepage')

def delete_confirmation(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/delete_account.html')

def delete_account(request, user_id):
    if request.method == "POST":
        delete_user = User.objects.get(id = user_id)
        delete_user.delete()
        return redirect('/')

def view_goals(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/goals.html')

def set_goal(request):
    if request.method == "POST":
        user = User.objects.get(id = request.session['userid'])
        title = request.POST['title']
        coins = request.POST['coin_worth']
        Goal.objects.create(user = user, title = title, coin_worth = coins)
        return redirect('/goals')

def edit_goal(request, goal_id):
    if request.method == "POST":
        edit_goal = Goal.objects.get(id = goal_id)
        edit_goal.title = request.POST['title']
        edit_goal.coin_worth = request.POST['coin_worth']
        edit_goal.save()
        return redirect('/goals')

def set_main_objective(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        user = User.objects.get(id = request.session['userid'])
        Main_Goal.objects.create(title = title, desc = desc, user = user)
        return redirect('/goals')

def goal_met(request):
    if request.method == "POST":
        return redirect('/')

def delete_goal(request, goal_id):
    if request.method == 'POST':

        return redirect('/goals')

def delete_main_goal(request, goal_id):
    if request.method == "POST":
        delete_goal = Main_Goal.objects.get(id = goal_id)
        delete_goal.delete()
    return redirect('/goals')

def journal(request):
    if request.method == "GET":
        return render (request, 'mental_illness_app/past_entries.html')

def new_journal(request):
    if request.method == "GET":
        return render (request, 'mental_illness_app/journal.html')

def process_journal(request):
    if request.method == "POST":
        user = User.objects.get(id = request.session['userid'])
        journal_name = request.POST['journal_name']
        rating = request.POST['rating']
        journal_entry = request.POST['entry']
        positive = request.POST['positive']
        Journal.objects.create(user = user, journal_name = journal_name, rating = rating, entry = journal_entry, positive = positive)
        return redirect('/journals')

def edit_journal(request, journal_id):
    if request.method == "POST":
        edit_journal = Journal.objects.get(id = journal_id)
        edit_journal.journal_name = request.POST['journal_name']
        edit_journal.rating = request.POST['rating']
        edit_journal.journal_entry = request.POST['entry']
        edit_journal.positive_thing = request.POST['positive']
        edit_journal.save()
        return redirect('/journals')

def update_journal(request, journal_id):
    if request.method == "GET":
        return render('mental_illness_app/edit_journal.html')

def delete_journal(request, journal_id):
    if request.method == "POST":
        delete_journal = Journal.objects.get(id = journal_id)
        delete_journal.delete()
        return redirect('/journals')

def drawing(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/drawing.html')

def panic_attack(request):
    if request.method == "GET":
        return render(request, 'mental_illness_app/panic_attack.html')
