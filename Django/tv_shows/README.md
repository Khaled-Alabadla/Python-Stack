# TV Shows Django App

This Django app implements CRUD routes for TV shows.

Routes implemented:

- `/` -> redirects to `/shows/`
- `/shows/` (GET) -> list all shows
- `/shows/new` (GET) -> form to add a new show
- `/shows/create` (POST) -> create a show and redirect to `/shows/`
- `/shows/<id>/` (GET) -> show details for specific show
- `/shows/<id>/edit` (GET) -> form to edit a show
- `/shows/<id>/update` (POST) -> update show then redirect to `/shows/`
- `/shows/<id>/destroy` (POST) -> delete show then redirect to `/shows/`
