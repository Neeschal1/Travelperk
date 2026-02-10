# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

# def update_password(email, password):
#     existing_email = User.email
#     try:
#         user = User.objects.get(existing_email = email)
#     except User.DoesNotExist:
#         raise ValidationError({'Message':f'Some eror occured. Try again!'})
    
#     user.password = password
#     return user.password