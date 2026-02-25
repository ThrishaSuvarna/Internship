import random

print(" Welcome to RoboController 1.0 \n")

# --- User Inputs ---
robot_name = input("Enter the robot's name: ")
distance_to_target = int(input("Enter distance to target (in meters): "))
obstacle = input("Is there an obstacle ahead? (yes/no): ").lower()

# --- Decision Making ---
speed = 0
movement = ""

if obstacle == "yes":
    if distance_to_target > 50:
        speed = 2
        movement = "Slow and cautious"
    else:
        speed = 1
        movement = "Very slow - obstacle nearby"
else:
    if distance_to_target > 100:
        speed = 10
        movement = "Fast forward"
    elif distance_to_target > 50:
        speed = 6
        movement = "Moderate speed"
    else:
        speed = 3
        movement = "Careful approach"

print(f"\n Movement Mode: {movement}")
print(f" Speed set to {speed} m/s")

# --- Journey Tracking ---
checkpoints = []
distance_travelled = 0

while distance_travelled < distance_to_target:
    step = random.randint(5, 20)
    distance_travelled += step

    direction_change = random.choice(["Straight", "Left", "Right"])
    checkpoint = f"{direction_change} turn at {distance_travelled}m"
    checkpoints.append(checkpoint)

    print(f" Checkpoint added: {checkpoint}")

    if distance_travelled >= distance_to_target:
        break

# --- Update Checkpoints ---
update = input("\nDo you want to remove the last checkpoint? (yes/no): ").lower()
if update == "yes" and checkpoints:
    removed = checkpoints.pop()
    print(f" Removed checkpoint: {removed}")

# --- Trip Summary ---
print("\n TRIP SUMMARY")
print("-" * 30)
print(f" Robot Name        : {robot_name}")
print(f" Target Distance   : {distance_to_target} meters")
print(f" Distance Travelled: {distance_travelled} meters")
print(f" Obstacle Ahead    : {obstacle.capitalize()}")
print(f" Final Checkpoints : {checkpoints}")
print("\n Mission Completed Successfully!")