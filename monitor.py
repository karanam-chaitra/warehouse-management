import time
import random

def check_system_health():
    print("Starting 10-minute monitoring session...")
    threshold = 0.05  # Alert threshold in seconds
    
    for minute in range(1, 11):
        # Simulate network/processing delay
        response_time = random.uniform(0.01, 0.08) 
        log_entry = f"Minute {minute:02d} | Response Time: {response_time:.4f}s"
        
        if response_time > threshold:
            log_entry += " *** ALERT: Threshold Exceeded! ***"
            
        print(log_entry)

if __name__ == '__main__':
    check_system_health()
