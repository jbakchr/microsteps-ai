import threading
import itertools
import sys
import time

from microsteps.core.generate import generate_microsteps  # ✅ NEW

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


def main():
    # ✅ Input (unchanged)
    task = input(BOLD + "What do you want to do?\n\n> " + RESET)

    # ✅ Start spinner
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner, args=(stop_event,))
    spinner_thread.start()

    try:
        # ✅ NEW: call local core instead of backend
        steps = generate_microsteps(task)

    finally:
        # ✅ Always stop spinner (even if something fails)
        stop_event.set()
        spinner_thread.join()

    line = "=" * 50

    print("\n" + line)
    print(BOLD + "START HERE" + RESET)
    print(line + "\n")

    for i, step in enumerate(steps, start=1):
        if i == 1:
            print(f"👉 Step {i}: {step}")
            print()
        else:
            print(f"   Step {i}: {step}")

    print("\n" + line + "\n")


if __name__ == "__main__":
    main()