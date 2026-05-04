# User Dashboard ERD

This document outlines the database schema for the User Dashboard application, based on the provided wireframes.

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    USERS ||--o{ MESSAGES : "posts"
    USERS ||--o{ MESSAGES : "receives"
    USERS ||--o{ COMMENTS : "replies"
    MESSAGES ||--o{ COMMENTS : "has"

    USERS {
        int id PK
        string first_name
        string last_name
        string email
        string password
        text description
        tinyint user_level
        datetime created_at
        datetime updated_at
    }

    MESSAGES {
        int id PK
        int user_id FK
        int recipient_id FK
        text content
        datetime created_at
        datetime updated_at
    }

    COMMENTS {
        int id PK
        int user_id FK
        int message_id FK
        text content
        datetime created_at
        datetime updated_at
    }
```

## Tables and Relationships

### 1. `users` Table

Stores information for all registered users, including admins and normal users

- **id**: Primary Key
- **first_name / last_name**
- **email**
- **password**
- **description**
- **user_level**: Determines permissions (Admin vs. Normal)
- **Timestamps**: `created_at` and `updated_at`

### 2. `messages` Table

- **id**: Primary Key
- **user_id**: Sender ID
- **recipient_id**: Receiver ID
- **content**
- **Timestamps**: `created_at` and `updated_at`

### 3. `comments` Table

- **id**: Primary Key
- **user_id**: Author ID
- **message_id**: Message ID
- **content**: Text
- **Timestamps**: `created_at` and `updated_at`

---

## Relationship Summary

- **User to Sent Messages**: 1 to Many
- **User to Received Messages**: 1 to Many
- **User to Comments**: 1 to Many
- **Message to Comments**: 1 to Many

---

## Functionality Mapping

To ensure the ERD fits the application functionality, the following actions are mapped to the database structure:

| Action       | Table(s) Involved | Logic/Notes    |
| :----------- | :---------------- | :------------- |
| **Register** | `users`           | New user       |
| **Login**    | `users`           | Auth           |
| **Post**     | `messages`        | Create message |
| **Reply**    | `comments`        | Create comment |
| **Admin**    | `users`           | Manage users   |
