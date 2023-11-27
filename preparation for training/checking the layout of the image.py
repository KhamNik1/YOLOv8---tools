import cv2
import numpy as np
import os

def draw_polygons_on_image(image_path, path):
    image = cv2.imread(os.path.join(path, 'images', image_path))

    if image is None:
        raise ValueError(f"Failed to load image from {image_path}")

    height, width, _ = image.shape

    # Get the path to the .txt file
    base_name = os.path.splitext(image_path)[0] + '.txt'
    txt_path = os.path.join(path, 'labels', base_name)

    # Dictionary to map label_id to color
    colors = {
        0: (0, 0, 255),  # Red
        1: (0, 255, 0),  # Green
        2: (255, 0, 0),  # Blue
        3: (0, 255, 255),  # Yellow
        4: (255, 0, 255),  # Magenta
        5: (255, 255, 0),  # Cyan
        6: (128, 128, 0),  # Olive
        7: (0, 128, 128),  # Dark cyan
        8: (128, 0, 128),  # Purple
        9: (0, 0, 0)  # Black
    }

    object_names = {
        0: 'Agricultural object',
        1: 'Fields',
        2: 'Forest',
        3: 'Grassland',
        4: 'Buildings',
        5: 'Power lines',
        6: 'Road',
        7: 'Water'
    }

    # Read coordinates from the file and draw polygons
    with open(txt_path, 'r') as file:
        for line in file:
            numbers = list(map(float, line.strip().split()))

            # Get label_id and corresponding color
            label_id = int(numbers[0])
            color = colors.get(label_id, (105, 105, 105))  # default color if label_id not found
            obj_name = object_names.get(label_id)

            # Get coordinates pairwise
            coords = [(numbers[i], numbers[i + 1]) for i in range(1, len(numbers), 2)]

            # Transform coordinates
            transformed_coords = [(int(x * width), int(y * height)) for x, y in coords]

            if height > 1152:
                fnt = 4
                thk = 4
                thickness = 8
            elif 640 < height < 1152:
                fnt = 2
                thk = 2
                thickness = 5
            else:
                fnt = 0.8
                thk = 2
                thickness = 3

            # Draw polygon on the image
            cv2.polylines(image, [np.array(transformed_coords)], isClosed=True, color=color, thickness=thickness)

            # Draw legend on the image
            # Calculate average coordinates for placing the text
            avg_x = int(sum(x for x, y in transformed_coords) / len(transformed_coords))
            avg_y = int(sum(y for x, y in transformed_coords) / len(transformed_coords))
            # Place the class name on the image
            cv2.putText(image, obj_name, (avg_x, avg_y), cv2.FONT_HERSHEY_SIMPLEX, fnt, color, thk, cv2.LINE_AA)

    # Save and display the result
    output_dir = os.path.join(path, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'output_' + os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Processed: {image_path} -> {output_path}")

# Path to the folder with images
path = 'C:\\Users\\Nikita\\Desktop\\train'
images = os.listdir(os.path.join(path, 'images'))

num = 1
for image in images:
    print(f"Processing image {num} out of {len(images)}")
    draw_polygons_on_image(image, path)
    num += 1
