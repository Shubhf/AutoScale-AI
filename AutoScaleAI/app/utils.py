# app/utils.py
import psutil
import logging

def get_system_stats():
    return psutil.cpu_percent(interval=0.1), psutil.virtual_memory().percent

def format_latency(seconds):
    return round(seconds * 1000, 2)

def setup_logger(log_file="autoscaler.log"):
    logger = logging.getLogger("AutoScaleAI")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def validate_input(features, expected_dim=64):
    if not isinstance(features, list):
        raise ValueError("Input must be a list.")
    if len(features) != expected_dim:
        raise ValueError(f"Expected {expected_dim} features, got {len(features)}")
