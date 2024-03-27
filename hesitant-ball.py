import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import threading
import time
import Ball

def close_plot():
    plt.pause(10)
    plt.close()

# Define circle parameters
circle_radius = 5

# Create figure and axis
fig, ax = plt.subplots()

# Set axis background color to black
ax.set_facecolor('black')

# Draw circle
circle = Circle((0, 0), circle_radius, edgecolor='white', facecolor='black')
ax.add_patch(circle)

# Define ball parameters
my_ball = Ball.Ball(size=0.1, weight=10, direction=(0, -1), speed=10, height=5, kinetic=500, gpe=500)

# Initial position of the ball
ball_x = 0
ball_y = circle_radius - my_ball.size  # Start at 12 o'clock position

# Draw ball
ball = plt.Circle((ball_x, ball_y), my_ball.size, color='gray')
ax.add_artist(ball)

# Set axis limits
ax.set_xlim(-circle_radius - 1, circle_radius + 1)
ax.set_ylim(-circle_radius - 1, circle_radius + 1)

# Set aspect ratio to equal to make the circle circular
ax.set_aspect('equal', adjustable='box')

# Function to update ball position
def update_position():
    while True:
        # Calculate new position based on direction and speed
        delta_x, delta_y = my_ball.direction
        ball_x += delta_x * my_ball.speed
        ball_y += delta_y * my_ball.speed
        
        # Ensure the ball stays within the circle
        ball_x %= (2 * circle_radius)
        ball_y %= (2 * circle_radius)
        
        # Update ball position
        ball.set_center((ball_x, ball_y))
        plt.pause(0.1)  # Pause to visualize the movement
        
# Start a thread to update ball position
thread = threading.Thread(target=update_position)
thread.start()

# Show plot
plt.grid(True)
plt.show()

# Start a thread to close the plot after 10 seconds
thread = threading.Thread(target=close_plot)
thread.start()
