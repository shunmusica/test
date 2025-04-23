
import yaml
import sys
import os

# Load YAML resource file
with open('resources.yaml', 'r') as file:
    data = yaml.safe_load(file)

total = data['total']
used = data['used']

# Incoming request via environment variables (can be set in GitLab CI)
requested = {
    "cpu": int(os.getenv("VM_CPU", "0")),
    "ram": int(os.getenv("VM_RAM", "0")),
    "gpu": int(os.getenv("VM_GPU", "0"))
}

# Calculate available resources
available = {k: total[k] - used.get(k, 0) for k in total}

# Print for logging
print("Available Resources:", available)
print("Requested Resources:", requested)

# Check if request can be fulfilled
for key in requested:
    if requested[key] > available[key]:
        print(f"❌ Not enough {key.upper()}: Requested {requested[key]}, Available {available[key]}")
        sys.exit(1)

print("✅ All requested resources are available. Proceeding with deployment.")
