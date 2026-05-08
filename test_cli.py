import requests

task = input("What do you want to do? ")

response = requests.post(
    "http://localhost:8006/generate-microsteps",
    json={"task": task}
)

data = response.json()

print("\nMicro-steps:\n")

for step in data["microsteps"]:
    print(f"- {step}")