# Django OAuth Toolkit Project

This project demonstrates a full implementation of **OAuth2** and **OpenID Connect (OIDC)** flows using **Django OAuth Toolkit (DOT)**.  
It includes:

- Application management (create, update, delete apps)
- Token management (list and revoke access tokens)
- Function-based protected resources
- Class-based protected resources with mixins
- Base OAuth2 views (Authorization, Token, Revoke)
- OIDC support (OIDCOnlyMixin, OIDCLogoutOnlyMixin)
- Customizable templates

---

## 📦 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd oauth_demo

2. Create a virtual environment and activate it:

python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Create a superuser:

python manage.py createsuperuser

6.Run the development server:

python manage.py runserver

oauth_demo/
├─ oauth_demo/
│  ├─ settings.py
│  ├─ urls.py
├─ accounts/           # User management
├─ api/                # Protected resource APIs
├─ oauth/              # OAuth2 apps + templates
│  ├─ templates/oauth2_provider/
│  │   ├─ base.html
│  │   ├─ authorize.html
│  │   ├─ application_list.html
│  │   ├─ application_form.html
│  │   ├─ application_registration_form.html
│  │   ├─ application_detail.html
│  │   ├─ application_confirm_delete.html
│  │   ├─ authorized-tokens.html
│  │   └─ authorized-token-delete.html
│  ├─ urls.py
│  └─ views.py
├─ api/
│  ├─ urls.py
│  └─ views.py
├─ manage.py
```
🔑 Using OAuth2 Views
1. Application Management Views

List applications: /oauth/applications/

Register new application: /oauth/applications/register/

Application detail: /oauth/applications/<id>/

Update application: /oauth/applications/<id>/update/

Delete application: /oauth/applications/<id>/delete/

These views are subclassed with ApplicationOwnerIsUserMixin to ensure users manage only their own applications.

2. Token Management Views

List authorized tokens: /oauth/tokens/

Revoke a token: /oauth/tokens/<id>/delete/

3. Function-Based Protected Resources

Read-only: @protected_resource()

Read/write: @rw_protected_resource()

Example:
```bash
@protected_resource()
def books_list(request):
    return JsonResponse({"books": [{"id":1,"title":"Django"}]})

4. Class-Based Protected Resources

Mixins available:

ProtectedResourceMixin → read-only token access

ReadWriteScopedResourceMixin → read/write scoped token

ScopedResourceMixin → custom scope handling

ClientProtectedResourceMixin → client credentials protection

OIDCOnlyMixin → OIDC-only access

OIDCLogoutOnlyMixin → OIDC logout handling

Example:

class ProtectedBooksView(ProtectedResourceMixin, APIView):
    def get(self, request):
        return Response({"books": ["Django","DRF"]})
```
5. Base OAuth2 Views

Authorization endpoint: AuthorizationView → /o/authorize/

Token endpoint: TokenView → /o/token/

Revoke token endpoint: RevokeTokenView → /o/revoke_token/

These handle the main OAuth2 flows: Authorization Code, Password, Client Credentials, and Refresh Tokens.

🖼 Templates

Templates are located in oauth/templates/oauth2_provider/ and can be overridden.

base.html → base layout

authorize.html → authorization form

application_list.html → list apps

application_registration_form.html → register app

application_form.html → update app

application_detail.html → app details

application_confirm_delete.html → delete app confirmation

authorized-tokens.html → list tokens

authorized-token-delete.html → revoke token

Example usage in authorize.html:

```bash
{% extends "oauth2_provider/base.html" %}

{% block content %}
<h3>Authorize {{ application.name }}?</h3>
<form method="post">{% csrf_token %}
<input type="submit" name="allow" value="Authorize"/>
</form>
{% endblock %}

🧪 Testing OAuth2 Flows

Obtain a token using client credentials or password grant:

curl -X POST -d "grant_type=password&username=<user>&password=<pass>&client_id=<id>&client_secret=<secret>" http://localhost:8000/o/token/


Access a protected resource:

curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://localhost:8000/api/books/

⚡ Notes

All views respect user ownership via ApplicationOwnerIsUserMixin.

CBVs support scopes for fine-grained access.

DOT provides models: Application, AccessToken, RefreshToken, Grant, IDToken.

OIDC mixins allow endpoints restricted to OpenID Connect flows.

📖 References

Django OAuth Toolkit Documentation

RFC6749 - OAuth2

RFC7662 - OAuth2 Token Introspection

OIDC RP-Initiated Logout


---

If you want, I can also **write a ready-to-use `requirements.txt` and minimal working template files** for this README so someone can clone and run the OAuth2 server immediately.  

Do you want me to do that next?```