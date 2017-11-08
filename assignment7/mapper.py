import sys

for line in sys.stdin:
    method = line.strip()
    if "HTTP" in method:
        print method
