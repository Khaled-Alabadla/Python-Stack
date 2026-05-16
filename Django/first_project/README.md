# first_project

Simple Django project with a single app `my_app`.

Routes (defined in `my_app/urls.py`):

- `/` -> redirects to `/blogs/` (view: `root`)
- `/blogs/` -> list placeholder (view: `index`)
- `/blogs/new` -> new form placeholder (view: `new`)
- `/blogs/create` -> redirects to `/` (view: `create`)
- `/blogs/json` -> returns JSON with `title` and `content` (view: `json_view`)
- `/blogs/<number>/` -> show placeholder (view: `show`)
- `/blogs/<number>/edit` -> edit placeholder (view: `edit`)
- `/blogs/<number>/delete` -> redirects to `/blogs/` (view: `destroy`)

Run the development server:

1. Create and activate a virtual environment (optional but recommended):
   - Windows PowerShell:
     ```powershell
     python -m venv env_name;
     ```

2. Install dependencies (if not already installed):

   ```powershell
   python -m pip install django
   ```

3. Run the server:

   ```powershell
   python manage.py runserver
   ```

Then open http://localhost:8000/ in your browser.
