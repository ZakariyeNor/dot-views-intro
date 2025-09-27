from django.shortcuts import render

from django.http import JsonResponse
from oauth2_provider.decorators import protected_resource, rw_protected_resource

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from oauth2_provider.views.mixins import (
    ProtectedResourceMixin,
    ReadWriteScopedResourceMixin,
    ScopedResourceMixin,
    ClientProtectedResourceMixin
)


from oauth2_provider.views.mixins import OIDCOnlyMixin, OIDCLogoutOnlyMixin
from rest_framework.views import APIView
from rest_framework.response import Response

# Only accessible via OpenID Connect flow
class OIDCBooksView(OIDCOnlyMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "This endpoint requires OIDC authentication."
        })

# Handles logout requests via OIDC
class OIDCLogoutView(OIDCLogoutOnlyMixin, APIView):
    def post(self, request, *args, **kwargs):
        # DOT handles token revocation and logout logic
        return Response({"message": "Successfully logged out via OIDC"})


# Read-only protected resource
class ProtectedBooksView(ProtectedResourceMixin, APIView):
    def get(self, request, *args, **kwargs):
        books = [
            {"id": 1, "title": "Django for Beginners"},
            {"id": 2, "title": "REST APIs with Django"},
        ]
        return Response({"books": books})

# Read/write protected resource (requires scope)
class ManageBooksView(ReadWriteScopedResourceMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Read-only access granted"})

    def post(self, request, *args, **kwargs):
        return Response({"message": "Book created"}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        return Response({"message": "Book updated"})

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Book deleted"}, status=status.HTTP_204_NO_CONTENT)

class CustomScopeBooksView(ScopedResourceMixin, APIView):
    required_scopes = ["books.read", "books.write"]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Scoped access granted"})

class ClientProtectedBooksView(ClientProtectedResourceMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Client-based token access"})


# Simple read-only protected endpoint
@protected_resource()
def books_list(request):
    books = [
        {"id": 1, "title": "Django for Beginners"},
        {"id": 2, "title": "REST APIs with Django"},
    ]
    return JsonResponse({"books": books})

# Read/write protected endpoint
@rw_protected_resource()
def books_manage(request):
    if request.method == "POST":
        return JsonResponse({"message": "Book created (dummy response)"})
    elif request.method == "PUT":
        return JsonResponse({"message": "Book updated (dummy response)"})
    elif request.method == "DELETE":
        return JsonResponse({"message": "Book deleted (dummy response)"})
    else:
        return JsonResponse({"message": "Unsupported method"}, status=405)
