import requests

task = input("What do you want to do? ")

response = requests.post(
    "http://localhost:8006/generate-microsteps",
    json={"task": task}
)

data = response.json()

# ✅ Clear separation
print("\n" + "=" * 40)
print("YOUR INPUT:")
print(f"{task}")
print("=" * 40)

print("\n--- MICRO-STEPS ---\n")
print("Start here:\n")

for i, step in enumerate(data["microsteps"], start=1):
    if i == 1:
        print(f"👉 Step {i}: {step}")
    else:
        print(f"   Step {i}: {step}")

print("\n" + "=" * 40 + "\n")