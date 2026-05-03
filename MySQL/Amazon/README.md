# Amazon Product Catalog ERD

This project defines the database schema for a product catalog based on the provided wireframe, which allows browsing products by **Brand**, **Category**, and **Character**.

## Database Schema Details

### 1. `brands` Table
Stores the manufacturers or brands of the products
- `id`: Primary Key
- `name`

### 2. `categories` Table
Stores product categories and supports a hierarchical structure (parent/child)
- `id`: Primary Key
- `name`
- `parent_id`: Reference to a parent category

### 3. `characters` Table
Stores characters that products might be associated with
- `id`: Primary Key
- `name`

### 4. `products` Table
The central table containing product information and linking to the other dimensions
- `id`: Primary Key
- `name
- `description
- `price
- `brand_id`: Foreign Key linking to the `brands` table
- `category_id`: Foreign Key linking to the `categories` table
- `character_id`: Foreign Key linking to the `characters` table
