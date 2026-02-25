import random
import time

print("=== RoboController 2.0 ===\n")

# User Inputs
robot_name = input("Enter Robot Name: ")
total_distance = float(input("Enter distance to target (in meters): "))
remaining_distance = total_distance

# Decide Speed
if total_distance > 150:
    speed = 30
elif 80 <= total_distance <= 150:
    speed = 20
else:
    speed = 10

checkpoints = ["Start"]

print("\nRobot started moving...\n")

# Continuous movement loop
while remaining_distance > 0:
    
    print(f"Remaining Distance: {remaining_distance} meters")
    
    obstacle = input("Is there an obstacle? (none/human/wall): ").lower()
    
    if obstacle == "human":
        print("👤 Human detected! Waiting...")
        time.sleep(2)
        checkpoints.append("Waited for Human")
    
    elif obstacle == "wall":
        print("🧱 Wall detected! Changing direction...")
        directions = ["Left", "Right", "Forward", "Backward"]
        turn = random.choice(directions)
        print(f"Turned {turn}")
        checkpoints.append(f"Turned {turn}")
    
    else:
        print("No obstacle. Moving forward...")
        checkpoints.append("Moved Forward")
    
    # Robot moves forward after handling obstacle
    remaining_distance -= speed
    
    if remaining_distance < 0:
        remaining_distance = 0
    
    print("-" * 40)

checkpoints.append("Target Reached")

# Final Trip Summary
print("\n=== Final Trip Summary ===")
print(f"Robot Name: {robot_name}")
print(f"Total Distance Travelled: {total_distance} meters")
print(f"Speed per Move: {speed} meters")
print(f"Final Checkpoints: {checkpoints}")