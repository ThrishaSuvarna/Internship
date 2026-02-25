import random
print("🤖 Welcome to RoboController 1.0 \n")
# Taking user inputs
robot_name = input("Enter robot name: ")
distance = int(input("Enter distance to target (in meters): "))
obstacle = input("Is there an obstacle ahead? (yes/no): ").lower()

# Decide speed using if-elif-else
if distance > 100:
    speed = "Fast"
elif distance > 50:
    speed = "Medium"
else:
    speed = "Slow"

# Nested if for obstacle handling
if obstacle == "yes":
    if speed == "Fast":
        action = "Slow down and turn"
    else:
        action = "Carefully move forward"
else:
    action = "Move straight"

# List to store checkpoints
checkpoints = []
checkpoints.append("Start Point")

# Simulating movement with random direction change
directions = ["Left", "Right", "Forward"]
random_direction = random.choice(directions)
checkpoints.append(f"Moved {random_direction}")

# Add final checkpoint
checkpoints.append("Target Reached")

# Example of removing a checkpoint (optional update)
if "Moved Left" in checkpoints:
    checkpoints.remove("Moved Left")

# Trip summary using f-strings
print("\n--- ROBOT TRIP SUMMARY ---")
print(f"Robot Name        : {robot_name}")
print(f"Total Distance    : {distance} meters")
print(f"Speed Selected    : {speed}")
print(f"Obstacle Ahead    : {obstacle}")
print(f"Action Taken      : {action}")
print(f"Checkpoints Visited: {checkpoints}")