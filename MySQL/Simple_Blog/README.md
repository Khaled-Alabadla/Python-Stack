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

## Relationships

- `users` to `posts`: One user can author many posts and the post belongs to one user (`users.id` → `posts.user_id`)
- `users` to `comments`: One user can write many comments and the comment belongs to one user (`users.id` → `comments.user_id`)
- `posts` to `comments`: One post can have many comments and the comment belongs to one post (`posts.id` → `comments.post_id`)
