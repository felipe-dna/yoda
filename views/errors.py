from django.http import JsonResponse



def missing_csrf_token_error_view(request, reason: str = ""):
    return JsonResponse({"message": "Missing csrf token."})

