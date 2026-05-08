import requests

task = input("What do you want to do? ")

response = requests.post(
    "http://localhost:8006/generate-microsteps",
    json={"task": task}
)

data = response.json()


print("\n--- Micro-steps ---")

print("\nStart here:\n")

for i, step in enumerate(data["microsteps"], start=1):
    if i == 1:
        print(f"👉 Step {i}: {step}")
    else:
        print(f"   Step {i}: {step}")

