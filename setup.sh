#!/bin/bash

# Seaker-Alert-App Setup Script
echo "Setting up Seaker-Alert-App..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
mkdir -p logs
mkdir -p config

# Build and start the application
echo "Building Docker images..."
docker-compose build

echo "Starting Seaker-Alert-App..."
docker-compose up -d

# Wait for services to start
echo "Waiting for services to start..."
sleep 30

# Check if services are running
echo "Checking service status..."
docker-compose ps

# Display access URLs
echo ""
echo "=== Seaker-Alert-App is Ready ==="
echo ""
echo "Access URLs:"
echo "  Grafana Dashboard: http://localhost:3000"
echo "  Web API: http://localhost:5000"
echo "  InfluxDB: http://localhost:8086"
echo ""
echo "Default Credentials:"
echo "  Grafana: admin/admin"
echo "  InfluxDB: admin/password123"
echo ""
echo "API Endpoints:"
echo "  GET  http://localhost:5000/health"
echo "  GET  http://localhost:5000/metrics"
echo "  GET  http://localhost:5000/thresholds"
echo "  POST http://localhost:5000/alerts/test"
echo ""
echo "To stop the application: docker-compose down"
echo "To view logs: docker-compose logs -f"
echo ""
