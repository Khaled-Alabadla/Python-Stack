# Yelp ERD

This project focuses on designing the database schema for a Yelp-like application based on a provided wireframe.

## Schema Details

### 1. Users Table

Stores information about the registered users who can write reviews

- `id`: Primary Key
- `first_name` & `last_name`
- `email`
- `password`
- `avatar`
- `created_at` / `updated_at`

### 2. Restaurants Table

Stores details about the restaurants listed on the platform

- `id`: Primary Key
- `name`
- `image_url`
- `created_at` / `updated_at`

### 3. Reviews Table

This table acts as a bridge (join) between users and restaurants, representing a **Many-to-Many** relationship

- `id`: Primary Key
- `content`
- `rating`: An integer (1-5) representing the star rating
- `user_id`: Foreign Key linking to the `users` table
- `restaurant_id`: Foreign Key linking to the `restaurants` table
- `created_at` / `updated_at`

## Relationships

- **Users to Reviews**: One-to-Many (A user can write multiple reviews).
- **Restaurants to Reviews**: One-to-Many (A restaurant can have multiple reviews).
- **Users to Restaurants**: Many-to-Many (Linked via the `reviews` table).
