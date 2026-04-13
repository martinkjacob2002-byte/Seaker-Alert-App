# Seaker Alert App

A simple system monitoring dashboard I built to track CPU, memory, disk usage, and other system metrics in real-time. It's got a nice web interface and can send alerts when things get too high.

## What It Does

- **Real-time Monitoring**: Shows CPU, memory, disk usage, uptime, and process count
- **Live Dashboard**: Updates every 3 seconds with current system stats
- **Alert System**: Sends notifications when metrics cross warning thresholds
- **Data Export**: Download metrics as JSON or CSV files
- **Historical Charts**: Visualize trends over time with interactive graphs

## Quick Start

### Option 1: Easy Windows Setup

Just double-click `run_app.bat` and it'll:
1. Check if Python is installed
2. Install the required packages
3. Start the web server
4. Open the dashboard in your browser

### Option 2: Manual Setup

1. Install Python 3.8+ if you don't have it
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python src/app.py`
4. Open http://localhost:5000 in your browser

### Option 3: Docker (if you're into that)

```bash
docker-compose up -d
```

Then visit http://localhost:5000

## Dashboard Features

The main dashboard shows:

- **CPU Cores**: Number of processor cores
- **CPU Usage**: Current CPU utilization with progress bar
- **Memory**: Used/Total memory in GB format
- **Memory Usage**: Percentage with color-coded progress bar
- **Disk**: Used/Total disk space in GB format  
- **Disk Usage**: Percentage with color-coded progress bar
- **Uptime**: How long the system has been running
- **Processes**: Number of running processes

The progress bars change color:
- Green: Below 70%
- Yellow: 70-89%
- Red: 90%+

## Configuration

You can tweak the alert thresholds in `config/app_config.json`:

```json
{
  "alerts": {
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
}
```

## API Endpoints

If you want to integrate with other tools:

- `GET /` - Basic app info
- `GET /health` - Health check
- `GET /metrics` - Current system metrics (JSON)
- `GET /alerts` - Current alert status
- `GET /export/csv` - Download metrics as CSV
- `GET /export/json` - Download metrics as JSON

## Project Structure

```
seaker-alert-app/
|-- src/
|   |-- app.py              # Main Flask application
|   |-- config_manager.py   # Handles configuration
|   |-- notification_service.py  # Alert notifications
|   `-- metrics_collector.py      # System metrics collection
|-- templates/
|   |-- index.html          # Main dashboard template
|   `-- dashboard.html     # Alternative dashboard
|-- static/
|   |-- css/
|   |   `-- styles.css     # Dashboard styles
|   `-- js/
|       `-- main.js         # Frontend JavaScript
|-- config/
|   `-- app_config.json    # Configuration file
|-- requirements.txt        # Python dependencies
|-- run_app.bat            # Windows quick start script
`-- README.md              # This file
```

## What I Used

- **Backend**: Flask (Python web framework)
- **Frontend**: Plain JavaScript with Chart.js for graphs
- **Styling**: CSS with some modern flexbox/grid
- **Metrics**: psutil library for system information
- **Database**: None needed for this demo version (stores in memory)

## Troubleshooting

### "Python not found" error
- Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

### Dashboard won't load
- Check if the server is running (look for "Starting Seaker Alert App..." message)
- Try refreshing the browser
- Check the console for error messages

### Port already in use
- Something else might be using port 5000
- Edit `src/app.py` and change the port number
- Or stop whatever's using port 5000

## Things I Might Add Later

- [ ] User authentication for dashboard access
- [ ] Email notifications for alerts
- [ ] More detailed system information
- [ ] Historical data storage in a real database
- [ ] Mobile app version
- [ ] Support for multiple machines

## Contributing

If you want to contribute or just play around with the code:

1. Fork the project
2. Make your changes
3. Test that everything still works
4. Send a pull request or just use it for your own stuff

## License

MIT License - do whatever you want with it, just don't blame me if it breaks stuff.

---

**Built with:** Python, Flask, Chart.js, and too much coffee  
**Dashboard URL:** http://localhost:5000 (when running)  
**Questions?** Feel free to open an issue or send a message.
