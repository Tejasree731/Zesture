import time

def log_action(action):
    with open("logs/gesture_log.txt", "a") as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp} - {action}\n")
