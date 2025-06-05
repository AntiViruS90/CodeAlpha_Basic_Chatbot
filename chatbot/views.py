from django.shortcuts import render
from django.http import JsonResponse
from .bot import get_response


def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        if not user_input:
            return JsonResponse({"response": "Please enter a message."})
        response = get_response(user_input)
        return JsonResponse({"response": response})
    return render(request, "chat.html")