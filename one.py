import random

def random_walk(steps):
    x, y = 0, 0  # Starting point
    distances = []  # List to store distances at each step

    for _ in range(steps):
        # Randomly choose a direction (up, down, left, or right)
        direction = random.choice(["up", "down", "left", "right"])

        # Update the position based on the chosen direction
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1

        # Calculate the distance from the starting point
        
        distance = abs(x) + abs(y)
        distances.append(distance)
        

    return distances

def main():
    steps = int(input("Enter the number of steps for the random walk: "))
    distances = random_walk(steps)

    # Calculate and print the average distance
    average_distance = sum(distances) / len(distances)
    print(f"Average distance from the starting point after {steps} steps: {average_distance:.2f}")

print(main())



my_list=[1,2,3]
print(sum(my_list))
print(len(my_list))