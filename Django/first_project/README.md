# first_project

Django project with three reusable apps: `blogs`, `surveys`, and `users`.

## Routes

### Blogs App (defined in `blogs/urls.py`)

- `/blogs` -> list all blogs (view: `index`)
- `/blogs/new` -> new blog form (view: `new`)
- `/blogs/create` -> create blog, redirects to `/blogs` (view: `create`)
- `/blogs/<number>` -> show specific blog (view: `show`)
- `/blogs/<number>/edit` -> edit blog form (view: `edit`)
- `/blogs/<number>/delete` -> delete blog, redirects to `/blogs` (view: `destroy`)

### Surveys App (defined in `surveys/urls.py`)

- `/surveys` -> list all surveys (view: `index`)
- `/surveys/new` -> new survey form (view: `new`)

### Users App (defined in `users/urls.py`)

- `/` -> redirects to `/blogs` (view: `index_root`)
- `/register` -> user registration form (view: `register`)
- `/login` -> user login form (view: `login`)
- `/users/new` -> alias for `/register` (view: `register`)
- `/users` -> list all users (view: `index`)
