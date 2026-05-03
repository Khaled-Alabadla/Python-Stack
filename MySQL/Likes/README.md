# Likes ERD

This document outlines the database structure based on the provided social media post wireframe.

## Table Details

### 1. `users`

Stores information about accounts that can post and interact.

- `id`: Primary Key, Auto-increment
- `name`: The display name
- `avatar_url`: The profile picture URL
- `created_at` & `updated_at`

### 2. `posts`

Stores the main posts created by users.

- `id`: Primary Key, Auto-increment
- `content`: The text content of the post
- `image_url`: The URL for the post's image
- `user_id`: Foreign Key linking to the author
- `created_at` & `updated_at`

### 3. `comments`

Stores user comments on specific posts.

- `id`: Primary Key, Auto-increment
- `content`: The text of the comment
- `user_id`: Foreign Key linking to the commenter
- `post_id`: Foreign Key linking to the parent post
- `created_at` & `updated_at`

### 4. `likes`

Tracks the many-to-many relationship of users liking posts.

- `id`: Primary Key, Auto-increment
- `user_id`: Foreign Key linking to the user who liked the post
- `post_id`: Foreign Key linking to the liked post
- `created_at` & `updated_at`

### 5. `shares`

Tracks users who share specific posts.

- `id`: Primary Key, Auto-increment
- `user_id`: Foreign Key linking to the user who shared the post
- `post_id`: Foreign Key linking to the shared post
- `created_at` & `updated_at`
