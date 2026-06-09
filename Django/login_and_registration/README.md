# Django Login and Registration

This is a Django application for user registration and login with both server-side and client-side validation.

## Features

- User registration with username, email, birthday, password, and password confirmation
- Server-side validation for email format, password length, password confirmation, unique email, birthday validity, and minimum age
- AJAX email uniqueness validation during registration
- Client-side JavaScript validation for required fields and form submission gating
- Login form validation for email format and required password
- Session-based success page access control

## Improvements & Suggestions

- Modern, minimal UI: templates were refactored to extend a simple `base.html` and use a compact `style.css` under `login_app/static/login_app/style.css`.
- Client-side validation: improved scripts to always prevent default submission until async checks finish.
- AJAX endpoint: `api/check-email/` returns JSON for email uniqueness checks; already implemented in `views.py`.
