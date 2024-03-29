#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""


import sys

# Define a dictionary to store counts for each status code
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Initialize total file size
total_size = 0
# Flag to track if 10 lines have been processed
line_count = 0

# Function to print statistics after 10 lines or interruption
def print_statistics():
  global total_size, line_count, status_counts
  print(f"Total file size: {total_size}")
  
  # Sort status codes for printing in ascending order
  sorted_codes = sorted(status_counts.keys())
  for code in sorted_codes:
    if status_counts[code] > 0:
      print(f"{code}: {status_counts[code]}")
  
  # Reset counters for next iteration
  line_count = 0
  status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
  for line in sys.stdin:
    # Check if line matches expected format
    if not line.strip():
      continue  # Skip empty lines
    parts = line.split()
    if len(parts) != 6 or not parts[2].startswith("GET") or not parts[5].isdigit():
      continue  # Skip lines not matching format
    
    # Extract data
    file_size = int(parts[5])
    status_code = int(parts[3])

    # Update counters
    total_size += file_size
    status_counts[status_code] += 1
    line_count += 1

    # Print statistics every 10 lines or on interruption
    if line_count % 10 == 0 or line_count == 1:
      print_statistics()

except KeyboardInterrupt:
  print("\nInterrupted. Printing statistics...")
  print_statistics()
