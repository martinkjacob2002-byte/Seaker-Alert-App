# Seaker-Alert-App

A comprehensive system monitoring and alerting application that tracks real-time system metrics with customizable thresholds and notifications.

## Overview

The Seaker-Alert-App monitors system usage metrics including CPU usage, memory, disk space, uptime, and temperature (when available). It provides a web-based dashboard for real-time visualization, historical data analysis, and configurable alerting system.

## Architecture

```
System Metrics -> Seaker-Alert-App -> InfluxDB -> Grafana Dashboard
                                    -> Alert Engine -> Notifications (Email/Slack)
```

## Features

- **Real-time Monitoring**: CPU, RAM, Disk, Uptime, Temperature
- **Web Dashboard**: Interactive Grafana dashboard with historical data
- **Customizable Alerts**: User-defined thresholds with multiple notification channels
- **Data Persistence**: Time-series database for historical analysis
- **Cross-platform**: Supports Windows, Linux, and Raspberry Pi
- **Containerized**: Easy deployment with Docker and Docker Compose

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Python 3.8+ (for local development)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Seaker-Alert-App.git
cd Seaker-Alert-App
```

2. Start the application:
```bash
docker-compose up -d
```

3. Access the dashboard:
- Grafana Dashboard: http://localhost:3000
- InfluxDB: http://localhost:8086

Default credentials:
- Grafana: admin/admin
- InfluxDB: admin/password123

## Project Structure

```
Seaker-Alert-App/
|-- docker-compose.yml
|-- Dockerfile
|-- README.md
|-- requirements.txt
|-- config/
|   |-- thresholds.json
|   |-- notifications.json
|-- src/
|   |-- metrics_collector.py
|   |-- alert_engine.py
|   |-- notification_service.py
|   |-- config_manager.py
|-- grafana/
|   |-- dashboards/
|   |   |-- system-metrics.json
|   |-- provisioning/
|   |   |-- dashboards/
|   |   |-- datasources/
|-- influxdb/
|   |-- init/
|   |   |-- init.iql
```

## Configuration

### Thresholds

Edit `config/thresholds.json` to customize alert thresholds:

```json
{
  "cpu_usage": {
    "warning": 70,
    "critical": 90
  },
  "memory_usage": {
    "warning": 80,
    "critical": 95
  },
  "disk_usage": {
    "warning": 85,
    "critical": 95
  },
  "temperature": {
    "warning": 70,
    "critical": 85
  }
}
```

### Notifications

Configure notification channels in `config/notifications.json`:

```json
{
  "email": {
    "enabled": true,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your-email@gmail.com",
    "password": "your-app-password",
    "recipients": ["admin@example.com"]
  },
  "slack": {
    "enabled": false,
    "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
  }
}
```

## Metrics Collected

| Metric | Description | Unit |
|--------|-------------|------|
| CPU Usage | Current CPU utilization | % |
| Memory Used | Current memory usage | GB |
| Memory Total | Total available memory | GB |
| Disk Used | Current disk usage | GB |
| Disk Total | Total disk space | GB |
| Uptime | System uptime | Hours |
| Temperature | System temperature (if available) | °C |

## Dashboard Access

**Live Dashboard URL**: http://localhost:3000/d/system-metrics/system-metrics-dashboard

The dashboard provides:
- Real-time metrics visualization
- Historical data analysis (last 24 hours, 7 days, 30 days)
- Interactive graphs and charts
- Alert status indicators
- Threshold configuration interface

## Alert Scenarios

### Example Alert Triggers

1. **High CPU Usage**: Alert when CPU > 90% for 5 minutes
2. **Low Memory**: Warning when RAM > 80%, Critical when RAM > 95%
3. **Disk Space**: Warning when disk > 85%, Critical when disk > 95%
4. **High Temperature**: Alert when temperature > 85°C (if available)

### Testing Alerts

To simulate an alert scenario:

1. Temporarily lower thresholds in `config/thresholds.json`
2. Monitor the dashboard for alert indicators
3. Check configured notification channels for alerts

## Development

### Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the metrics collector:
```bash
python src/metrics_collector.py
```

### Building Docker Image

```bash
docker build -t seaker-alert-app .
```

## API Endpoints

- `GET /metrics`: Current system metrics
- `GET /health`: Application health status
- `POST /thresholds`: Update alert thresholds
- `GET /alerts`: Active alerts status

## Export Options

The dashboard supports data export in:
- CSV format
- JSON format
- PDF reports

Access via Grafana dashboard export options.

## Security

- Change default passwords before production deployment
- Use environment variables for sensitive configuration
- Enable HTTPS for production deployments
- Implement role-based access control in Grafana

## Troubleshooting

### Common Issues

1. **InfluxDB connection failed**: Check if InfluxDB container is running
2. **Grafana not showing data**: Verify data source configuration
3. **Alerts not working**: Check notification service configuration

### Logs

View application logs:
```bash
docker-compose logs -f metrics-collector
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

## Live Demo

**Dashboard URL**: http://localhost:3000/d/system-metrics/system-metrics-dashboard

The live demo shows:
- Real-time system metrics
- Historical data visualization
- Alert configuration interface
- Notification testing capabilities

## Project Status: COMPLETE

### Features Implemented
- [x] **System Metrics Collection**: CPU, Memory, Disk, Uptime, Temperature
- [x] **Real-time Dashboard**: Grafana with interactive visualizations
- [x] **Alert System**: Customizable thresholds with multiple notification channels
- [x] **Data Persistence**: InfluxDB time-series database
- [x] **Web API**: RESTful API for metrics and configuration
- [x] **Containerization**: Docker and Docker Compose setup
- [x] **Documentation**: Comprehensive README and deployment guide
- [x] **Configuration Management**: JSON-based configuration files
- [x] **Export Options**: CSV and JSON data export
- [x] **Cross-platform Support**: Windows, Linux, Raspberry Pi

### Quick Start Commands
```bash
# Start the application
docker compose up -d

# Access dashboard
open http://localhost:3000

# Test alerts
curl -X POST http://localhost:5000/alerts/test \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "message": "Test alert", "level": "warning"}'
```

### Repository Structure
```
Seaker-Alert-App/
|-- README.md                    # Complete documentation
|-- DEPLOYMENT_GUIDE.md         # Step-by-step deployment guide
|-- docker-compose.yml          # Multi-service orchestration
|-- Dockerfile                   # Container build configuration
|-- requirements.txt             # Python dependencies
|-- setup.sh                     # Automated setup script
|-- test_local.py               # Local testing script
|-- config/                     # Configuration files
|   |-- thresholds.json         # Alert thresholds
|   |-- notifications.json      # Notification settings
|-- src/                        # Source code
|   |-- metrics_collector.py   # System metrics collection
|   |-- alert_engine.py         # Alert monitoring and processing
|   |-- notification_service.py # Multi-channel notifications
|   |-- config_manager.py       # Configuration management
|   |-- web_api.py              # REST API endpoints
|-- grafana/                    # Grafana configuration
|   |-- dashboards/             # Pre-configured dashboards
|   |-- provisioning/           # Auto-provisioning settings
|-- influxdb/                   # InfluxDB initialization
```

---

*Note: This application is designed for demonstration purposes. For production use, ensure proper security measures and scaling considerations are implemented.*
