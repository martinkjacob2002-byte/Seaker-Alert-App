#!/usr/bin/env python3
"""
Local test script for Seaker-Alert-App
Tests the components without Docker
"""

import sys
import os
import time
import json
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_metrics_collection():
    """Test metrics collection locally"""
    print("Testing metrics collection...")
    
    try:
        from metrics_collector import MetricsCollector
        
        # Create a mock collector (without InfluxDB)
        collector = MetricsCollector()
        
        # Test metric collection
        timestamp, metrics = collector.collect_all_metrics()
        
        print(f"Collected {len(metrics)} metrics at {timestamp}")
        print("Sample metrics:")
        for key, value in list(metrics.items())[:5]:
            print(f"  {key}: {value}")
            
        return True
    except Exception as e:
        print(f"Error in metrics collection: {e}")
        return False

def test_config_manager():
    """Test configuration management"""
    print("\nTesting configuration management...")
    
    try:
        from config_manager import ConfigManager
        
        config = ConfigManager()
        
        # Test thresholds
        thresholds = config.get_thresholds()
        print(f"Loaded thresholds: {json.dumps(thresholds, indent=2)}")
        
        # Test notifications
        notifications = config.get_notifications()
        print(f"Loaded notifications: {json.dumps(notifications, indent=2)}")
        
        return True
    except Exception as e:
        print(f"Error in configuration management: {e}")
        return False

def test_notification_service():
    """Test notification service"""
    print("\nTesting notification service...")
    
    try:
        from notification_service import NotificationService
        
        service = NotificationService()
        
        # Test console notification
        service.send_console_alert("Test Alert", "This is a test alert", "warning")
        
        return True
    except Exception as e:
        print(f"Error in notification service: {e}")
        return False

def test_alert_engine():
    """Test alert engine (without InfluxDB)"""
    print("\nTesting alert engine...")
    
    try:
        from alert_engine import AlertEngine
        
        # This will fail due to InfluxDB connection, but we can test the structure
        engine = AlertEngine()
        print("Alert engine created successfully")
        
        return True
    except Exception as e:
        print(f"Expected error (InfluxDB not available): {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Seaker-Alert-App Local Test Suite")
    print("=" * 60)
    
    tests = [
        ("Configuration Manager", test_config_manager),
        ("Notification Service", test_notification_service),
        ("Metrics Collection", test_metrics_collection),
        ("Alert Engine", test_alert_engine),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"Test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! The application components are working correctly.")
    else:
        print("Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main()
