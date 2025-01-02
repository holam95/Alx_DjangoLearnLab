from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == role
    return user_passes_test(decorator)