
# redirect nos permitira redirigir
from django.shortcuts import redirect
# invierte el valor del name por la url
from django.urls import reverse
# 
# Creamos una clase para implementar el middleware
class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_anonymous:
            # El user y el profile tienen una relacion 1 a 1 
            profile = request.user.profile
            # condicion para que se ejecute el middleware
            if not profile.picture or not profile.biography:

                # lista blanca para definir cuales url quedan fuera del middeleware
                if request.path not in [reverse('users:update_profile'),
                reverse('users:logout')] and not request.path.startswith(
                        '/admin/'):
                    return redirect('users:update_profile')
        response = self.get_response(request)
        return response