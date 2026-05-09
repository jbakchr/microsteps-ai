import requests
import threading
import itertools
import sys
import time

BOLD = "\033[1m"
RESET = "\033[0m"


def spinner(stop_event):
    print()
    for char in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\rThinking... {char}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")  # clean up line


# ✅ Input (with spacing as you liked)
task = input(BOLD + "What do you want to do?\n\n> " + RESET)

# ✅ Start spinner
stop_event = threading.Event()
spinner_thread = threading.Thread(target=spinner, args=(stop_event,))
spinner_thread.start()

# ✅ Make request
response = requests.post(
    "http://localhost:8006/generate-microsteps",
    json={"task": task}
)

# ✅ Stop spinner
stop_event.set()
spinner_thread.join()

data = response.json()

line = "=" * 50

print("\n" + line)
print(BOLD + "START HERE" + RESET)
print(line + "\n")

for i, step in enumerate(data["microsteps"], start=1):
    if i == 1:
        print(f"👉 Step {i}: {step}")
        print()
    else:
        print(f"   Step {i}: {step}")

print("\n" + line + "\n")