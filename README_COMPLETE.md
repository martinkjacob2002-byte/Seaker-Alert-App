# Seaker Alert App - System Monitoring & Alert Application

A comprehensive system monitoring and alerting application that tracks real-time system metrics with customizable thresholds and notifications.

## Overview

Seaker Alert App is a production-ready monitoring solution that provides:
- Real-time system metrics collection (CPU, Memory, Disk, Uptime, Temperature)
- Web-based dashboard with live visualizations
- Configurable alert thresholds with multiple notification channels
- Historical data storage and analysis
- Data export capabilities (JSON, CSV)
- Docker-based deployment for easy setup

## Features

### Core Metrics Monitoring
- **CPU Usage**: Real-time CPU utilization percentage
- **Memory**: Used and Total RAM in GB with usage percentage
- **Disk**: Used and Total disk space in GB with usage percentage
- **Uptime**: System uptime in hours
- **Temperature**: Device temperature (if available)
- **Process Count**: Number of running processes

### Dashboard Features
- **Real-time Updates**: 3-second auto-refresh with smooth transitions
- **Historical Charts**: Line graphs showing metric trends over time
- **Progress Bars**: Visual indicators with color-coded thresholds
- **Responsive Design**: Clean, professional interface that fits any screen
- **Export Options**: Download metrics as JSON or CSV files

### Alert System
- **Customizable Thresholds**: Configure alert levels for each metric
- **Multiple Channels**: Email, Slack, and on-screen notifications
- **Real-time Alerts**: Instant notifications when thresholds are exceeded
- **Alert History**: Track and view past alert events

### Data Persistence
- **InfluxDB**: Time-series database for historical data storage
- **Grafana**: Advanced visualization and analytics dashboard
- **Data Retention**: Configurable retention policies for historical data

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.8+ (for local development)
- Git

### Installation & Setup

#### Option 1: Docker Deployment (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Seaker-Alert-App
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access the applications**
   - **Main Dashboard**: http://localhost:5000/dashboard
   - **Grafana Dashboard**: http://localhost:3000 (admin/admin)
   - **API Documentation**: http://localhost:5000/api

#### Option 2: Local Development

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start InfluxDB**
   ```bash
   docker run -d -p 8086:8086 --name influxdb influxdb:2.0
   ```

3. **Run the application**
   ```bash
   cd src
   python demo_api.py
   ```

## Configuration

### Alert Thresholds

Configure alert thresholds via the dashboard or API:

```json
{
  "cpu_usage": {
    "warning": 70,
    "critical": 90
  },
  "memory_usage": {
    "warning": 75,
    "critical": 90
  },
  "disk_usage": {
    "warning": 80,
    "critical": 95
  }
}
```

### Email Notifications

Configure email settings in `config/config.json`:

```json
{
  "email": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your-email@gmail.com",
    "password": "your-app-password",
    "from_address": "alerts@seaker-app.com",
    "to_addresses": ["admin@company.com"]
  }
}
```

### Slack Integration

Add Slack webhook URL to configuration:

```json
{
  "slack": {
    "webhook_url": "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK",
    "channel": "#alerts",
    "username": "Seaker Alert Bot"
  }
}
```

## API Endpoints

### Metrics
- `GET /metrics` - Current system metrics
- `GET /metrics/history` - Historical metrics data

### Alerts
- `GET /alerts` - Current alert status
- `POST /alerts/test` - Send test alert
- `GET /thresholds` - Get alert thresholds
- `POST /thresholds` - Update alert thresholds

### Data Export
- `GET /export/json` - Export metrics as JSON
- `GET /export/csv` - Export metrics as CSV

### System
- `GET /health` - Health check
- `GET /api` - API documentation

## Example Usage

### Monitor System Metrics
```bash
curl http://localhost:5000/metrics
```

### Update Alert Thresholds
```bash
curl -X POST http://localhost:5000/thresholds \
  -H "Content-Type: application/json" \
  -d '{"cpu_usage": {"warning": 80, "critical": 95}}'
```

### Export Data
```bash
# JSON export
curl http://localhost:5000/export/json -o metrics.json

# CSV export
curl http://localhost:5000/export/csv -o metrics.csv
```

## Dashboard Access

### Live Dashboard URL
**http://localhost:5000/dashboard**

### Grafana Dashboard
**http://localhost:3000** (admin/admin)

### Features
- Real-time metric updates every 3 seconds
- Interactive charts with zoom and pan
- Color-coded progress bars (green/yellow/red)
- Export functionality for data analysis
- Mobile-responsive design

## Alert Scenarios

### Example Threshold Configurations

#### High Performance Environment
```json
{
  "cpu_usage": {"warning": 80, "critical": 95},
  "memory_usage": {"warning": 85, "critical": 95},
  "disk_usage": {"warning": 85, "critical": 95}
}
```

#### Development Environment
```json
{
  "cpu_usage": {"warning": 70, "critical": 90},
  "memory_usage": {"warning": 75, "critical": 90},
  "disk_usage": {"warning": 80, "critical": 90}
}
```

### Testing Alerts

1. **Via Dashboard**: Click "Test Alert" button
2. **Via API**: 
   ```bash
   curl -X POST http://localhost:5000/alerts/test \
     -H "Content-Type: application/json" \
     -d '{"title": "Test Alert", "message": "This is a test"}'
   ```

## Docker Configuration

### Services
- **seaker-api**: Main Flask application (Port 5000)
- **influxdb**: Time-series database (Port 8086)
- **grafana**: Visualization dashboard (Port 3000)

### Volumes
- `influxdb_data`: Persistent InfluxDB storage
- `grafana_data`: Persistent Grafana configuration

### Environment Variables
```yaml
environment:
  - INFLUXDB_URL=http://influxdb:8086
  - INFLUXDB_TOKEN=your-token
  - INFLUXDB_ORG=seaker-app
  - INFLUXDB_BUCKET=metrics
```

## Architecture

### Components
1. **Metrics Collector**: Python service using psutil
2. **API Server**: Flask REST API
3. **Web Dashboard**: Real-time JavaScript interface
4. **Database**: InfluxDB for time-series storage
5. **Visualization**: Grafana for advanced analytics
6. **Alert Engine**: Threshold monitoring and notifications

### Data Flow
```
System Metrics -> Collector -> InfluxDB -> API -> Dashboard
                        -> Alert Engine -> Notifications
```

## Security Considerations

- **API Authentication**: Configure API keys for production
- **HTTPS**: Use SSL/TLS certificates in production
- **Firewall**: Restrict access to monitoring ports
- **Data Encryption**: Encrypt sensitive configuration data

## Troubleshooting

### Common Issues

#### Dashboard Not Loading
```bash
# Check API status
curl http://localhost:5000/health

# Check logs
docker-compose logs seaker-api
```

#### Alerts Not Working
```bash
# Verify email configuration
curl -X POST http://localhost:5000/alerts/test

# Check alert thresholds
curl http://localhost:5000/thresholds
```

#### Grafana Connection Issues
```bash
# Check InfluxDB connection
docker-compose exec influxdb influx ping

# Verify Grafana configuration
docker-compose logs grafana
```

### Performance Tuning

#### Metrics Collection Interval
```python
# In src/metrics_collector.py
COLLECTION_INTERVAL = 30  # seconds
```

#### Data Retention
```sql
-- In InfluxDB
ALTER RETENTION POLICY "autogen" ON "metrics" DURATION 30d DEFAULT
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes and test
4. Submit pull request

## License

MIT License - see LICENSE file for details

## Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review API documentation at http://localhost:5000/api

## Version History

- **v1.0**: Initial release with core monitoring features
- **v1.1**: Added temperature monitoring and export functionality
- **v1.2**: Enhanced alert system and dashboard improvements

---

**Live Dashboard**: http://localhost:5000/dashboard  
**Grafana Dashboard**: http://localhost:3000  
**API Documentation**: http://localhost:5000/api
