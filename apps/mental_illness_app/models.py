from django.db import models

class Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password does not match confirmation."
        new_email = postData['email']
        if User.objects.filter(email=new_email).exists():
            errors['email'] = "Email is already in use, please use another email."
        if len(postData['name']) == 0:
            errors['name'] = "Please enter a name, even a false one!"
        if len(postData['password']) == 0:
            errors['password'] = "Please enter a password."
        if len(postData['email']) == 0:
            errors['email'] = "Please enter a email."
        return errors

# class Login_Manager(models.Manager):
#     def login_validator(self, postData):
#         login_errors = {}
#         if len(postData['email']) == 0:
#             login_errors['email'] = "Email is required to log in."
#         if len(postData['password']) == 0:
#             login_errors['password'] = "Password field is empty."
#         login_email = postData['email']
#         if User.objects.filter(email=login_email).exists() == False:
#             login_errors['email'] = "Email does not exist in database."

#         return login_errors

class Journal_Manager(models.Manager):
    def journal_validator(self, postData):
        journal_errors = {}
        if len(postData['journal_name']) == 0:
            journal_errors['journal_name'] = "Journal name is required."
        if len(postData['entry']) == 0:
            journal_errors['entry'] == "Entry is empty."
        if len(postData['positive']) == 0:
            journal_errors['positive'] = "Specify something that went well for you today!"
        
        return journal_errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coin_amount = models.IntegerField()
    objects = Manager()

class Goal(models.Model):
    title = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name="goal")
    coin_worth = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Main_Goal(models.Model):
    goal_title = models.CharField(max_length = 255)
    goal_desc = models.TextField(max_length = 255)
    coin_goal = models.IntegerField()
    user = models.ForeignKey(User, related_name='main_goal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Journal(models.Model):
    user = models.ForeignKey(User, related_name="journal")
    journal_name = models.CharField(max_length = 255)
    rating = models.CharField(max_length = 255)
    journal_entry = models.TextField()
    positive = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Journal_Manager()

