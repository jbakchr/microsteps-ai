import requests


BOLD = "\033[1m"
RESET = "\033[0m"


task = input(BOLD + "What do you want to do?\n\n> " + RESET)

response = requests.post(
    "http://localhost:8006/generate-microsteps",
    json={"task": task}
)

data = response.json()

print("\n" + "=" * 40)
print(BOLD + "START HERE" + RESET)
print("=" * 40 + "\n")

for i, step in enumerate(data["microsteps"], start=1):
    if i == 1:
        print(f"👉 Step {i}: {step}")
        print()  # extra space after step 1
    else:
        print(f"   Step {i}: {step}")

print("\n" + "=" * 40 + "\n")