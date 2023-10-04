import math

# Function to calculate camera distance
def calculate_camera_distance(focal_length, subject_height, horizon_height):
    return (subject_height * focal_length) / horizon_height

# Function to calculate camera height
def calculate_camera_height(subject_height, camera_distance, camera_angle):
    return subject_height - (camera_distance * math.tan(math.radians(camera_angle)))

# Function to calculate camera-to-subject distance
def calculate_camera_to_subject_distance(focal_length, camera_height, camera_angle):
    return camera_height / math.tan(math.radians(camera_angle))

# Input values
focal_length = float(input("Enter the focal length of your camera lens (in mm): "))
subject_height = float(input("Enter the height of the subject (in meters): "))
background_height = 4000  # Height of the digital background in pixels
horizon_percentage = 20  # Percentage of the background from the bottom where the horizon is
camera_height = float(input("Enter the height of the camera from the floor (in meters): "))
camera_angle = float(input("Enter the camera angle (in degrees): "))

# Calculate the height of the horizon in pixels
horizon_height = (horizon_percentage / 100) * background_height

# Calculate camera distance
camera_distance = calculate_camera_distance(focal_length, subject_height, horizon_height)

# Calculate camera height
camera_height = calculate_camera_height(subject_height, camera_distance, camera_angle)

# Calculate camera-to-subject distance
camera_to_subject_distance = calculate_camera_to_subject_distance(focal_length, camera_height, camera_angle)

# Display results
print(f"Camera Distance: {camera_distance:.2f} mm")
print(f"Camera Height: {camera_height:.2f} meters")
print(f"Camera-to-Subject Distance: {camera_to_subject_distance:.2f} meters")
