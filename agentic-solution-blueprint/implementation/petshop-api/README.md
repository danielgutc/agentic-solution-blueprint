name: PetShop API

description: A modern e-commerce web application for browsing, searching, and purchasing pet supplies and pets.

version: 1.0.0

license: MIT

keywords:
  - petshop
  - e-commerce
  - pet supplies
  - .NET
  - React
  - ASP.NET Core
  - PostgreSQL
  - Redis
  - RabbitMQ

repository: https://github.com/danielgutc/agentic-solution-blueprint

authors:
  - Daniel Gutierrez <dani.gutierrez@gmail.com>

structure:
  backend:
    path: implementation/petshop-api
    language: C# / .NET 8
    framework: ASP.NET Core Web API
  frontend:
    path: implementation/petshop-web
    language: TypeScript / React 18
    build_tool: Vite

technologies:
  backend:
    - .NET 8
    - ASP.NET Core 8
    - Entity Framework Core 8
    - PostgreSQL 16
    - Redis 7
    - RabbitMQ 3.13
    - Docker
    - Kubernetes
  frontend:
    - React 18
    - TypeScript
    - Vite
    - Zustand
    - React Router
    - Axios
  devops:
    - GitHub Actions
    - Docker
    - Kubernetes
    - Helm

tech_stack:
  - name: .NET 8
    version: "8.0"
  - name: React
    version: "18"
  - name: PostgreSQL
    version: "16"
  - name: Redis
    version: "7"
  - name: RabbitMQ
    version: "3.13"
