# Simple Blog ERD

This document outlines the database structure for the Simple Blog application.

## Database Schema

### ERD Diagram

```mermaid

    users {
        int id PK
        string first_name
        string last_name
        string email
        string password
        datetime created_at
        datetime updated_at
    }

    posts {
        int id PK
        text content
        int user_id FK
        datetime created_at
        datetime updated_at
    }

    comments {
        int id PK
        text content
        int user_id FK
        int post_id FK
        datetime created_at
        datetime updated_at
    }
```

## Table Details

### 1. `users`
Stores user account information.
- `id`: Primary Key, Auto-increment.
- `first_name` & `last_name`: Used for "Posted by" labels.
- `email`: Unique identifier for login.
- `password`: Hashed password string.

### 2. `posts`
Stores the main blog posts.
- `id`: Primary Key.
- `content`: The text of the post.
- `user_id`: Foreign Key linking to the author.

### 3. `comments`
Stores comments left on posts.
- `id`: Primary Key.
- `content`: The text of the comment.
- `user_id`: Foreign Key linking to the commenter.
- `post_id`: Foreign Key linking to the parent post.
