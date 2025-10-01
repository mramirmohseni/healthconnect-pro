# HealthConnect Pro

A healthcare appointment management system built with Django, PostgreSQL, Redis, and Docker.

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd healthconnect-pro
   ```

2. Create environment file:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your preferred values.

3. Start the application:
   ```bash
   docker compose up -d --build
   ```

4. Create a superuser:
   ```bash
   docker compose exec -it web python src/manage.py createsuperuser
   ```

5. Access the admin panel:
   - Open http://localhost:8000/admin/
   - Log in with your superuser credentials

### Development

#### Running the application
```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f web

# Stop services
docker compose stop

# Restart services
docker compose up -d
```

#### Database operations
```bash
# Run migrations
docker compose exec web python src/manage.py migrate

# Create superuser
docker compose exec -it web python src/manage.py createsuperuser

# Django shell
docker compose exec web python src/manage.py shell
```

### Services
- **web**: Django application (port 8000)
- **healthconnect_postgres**: PostgreSQL database (port 5432)
- **healthconnect_redis**: Redis cache (port 6379)

### Project Structure