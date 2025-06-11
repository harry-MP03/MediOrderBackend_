# En tu nuevo archivo middleware.py

class DebugRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("=========================================================")
        print("DEBUG: Petición entrante")
        print(f"  -> Path solicitado: {request.path}")
        print(f"  -> Método: {request.method}")
        print(f"  -> Usuario autenticado: {request.user.is_authenticated}")
        print(f"  -> Cookies: {request.COOKIES}")
        print("=========================================================")

        response = self.get_response(request)

        return response