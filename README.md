<h1>
  <img src="frontend/public/icon.png" width="32" style="vertical-align: middle; border-radius: 8px;" />
  Connect.
</h1>

Connect is a social media platform built with DRF & TS. Fully Responsive and minimalistic design.

<p align="center">
  <img src="https://img.shields.io/badge/coverage-85%25-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB&style=for-the-badge" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/DRF-092E20?logo=django&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white">
</p>

<div align="center">
  <img src="Banner.png" alt="preview" style="border-radius: 12px;" />
</div>

**Connect to your Friends and interact with them**

## Preview

<div align="center">
  <img src="Preview.gif" width="700" style="border-radius: 12px;" />
</div>

## 🚀 Tech Stack

| Logo                                                                                                                         | Technology                      | Intended Use                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" width="40"/>             | **React**                       | Frontend UI library for building dynamic, component-based user interfaces.   |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/reactrouter/reactrouter-original.svg" width="40"/> | **React Router**                | Client-side routing for navigating between pages without reloading.          |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" width="40" />      | **TailwindCSS**                 | Utility-first CSS framework for fast, responsive styling.                    |
| <img src="https://ui.shadcn.com/favicon.ico" width="32"/>                                                                    | **shadcn/ui**                   | High-quality headless UI components for consistent, modern interface design. |
| <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/zod.svg" width="40"/>                    | **Zod**                         | Schema validation + TypeScript inference for form data.                      |
| <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/reacthookform.svg" width="40"/>          | **React Hook Form**             | Fast, optimized form handling with built-in validation.                      |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" width="40"/>   | **TypeScript**                  | Strongly typed JavaScript for more robust frontend code.                     |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40"/>           | **Python**                      | Backend programming language to build the API logic.                         |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg" width="40"/>              | **Django REST Framework (DRF)** | Backend API framework for authentication, serialization & business logic.    |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytest/pytest-original.svg" width="40"/>           | **Pytest**                      | Testing backend logic, endpoints, models & utilities.                        |
| <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/jsonwebtokens.svg" width="40"/>          | **JWT**                         | Token-based authentication for secure login & session handling.              |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" width="40"/>         | **Postgres**                    | High Performance SQL Database.                                               |

## 🛢️ Database Schema

<div align="center">
  <img src="DatabaseSchema.png" alt="preview" style="border-radius: 12px;" />
</div>

## Features

- Create or Delete Account
- Login (JWT Authenticated)
- Add or Delete Post
- See Your Posts
- View Latests Post from the People you follow
- Update and Edit Profile
- Search for other Users
- Follow other Users
- See Following/ Follower List/Count

## Endpoints

- Swagger API docs `/api/v1/docs/`
- Register a user **POST** `/api/v1/register/`
- Login a user **POST** `/api/v1/login/`
- Refresh access token **POST** `/api/v1/refresh/`
- Get your or other User Profile Details **GET** `/api/v1/profile/`
- Update Profile Details **PATCH** `/api/v1/profile/`
- Delete your Profile **DELETE** `/api/v1/profile/`
- Post Feed **GET** `/api/v1/feed/`
- Search for other user **GET** `/api/v1/search/`
- Get Comments for a Post **GET** `/api/v1/comments/`
- Post a Comment on a Post **POST** `/api/v1/comments/`
- Add a Post **POST** `/api/v1/post/`
- Delete a Post **DELETE** `/api/v1/post/`
- Get all Post of a User **GET** `/api/v1/all_posts/`
- Get following list/count **GET** `/api/v1/following/`
- Follow a User **POST** `/api/v1/following/`
- Get Follower list/count **GET** `api/v1/follower/`

* For request/response structure visit api docs or _backend/api/v1/views/_

## Backend Setup

- cd backend/
- Create .env

  ```
  DEBUG = "True" | "False"
  DJANGO_ENV = "dev" | "prod"

  SECRET_KEY

  DEV_DB_NAME
  PROD_DB_NAME

  DB_USERNAME
  DB_PASSWORD

  DB_HOST
  DB_PORT

  ```

- Run `make venv`
- Then run `make migrate`
- Then run `make seed` for seeding database with fake users
- Then run `make run`

## Frontend Setup

- cd frontend/
- Create .env

  ```
  VITE_BASE_URL=http://localhost:8000/api/v1/

  VITE_IMAGE_URL=http://localhost:8000
  ```

  or change according to backend

- Run `npm install`
- Then `npm run dev`
