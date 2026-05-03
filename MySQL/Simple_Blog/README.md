# Simple Blog ERD

This document outlines the database structure for the Simple Blog application.

## Table Details

### 1. `users`

Stores user account information

- `id`: Primary Key, Auto-increment
- `first_name` & `last_name`
- `email`
- `password`

### 2. `posts`

Stores the main blog posts

- `id`: Primary Key
- `content`: The text of the post
- `user_id`: Foreign Key linking to the author

### 3. `comments`

Stores comments left on posts

- `id`: Primary Key
- `content`: The text of the comment
- `user_id`: Foreign Key linking to the commenter
- `post_id`: Foreign Key linking to the parent post
