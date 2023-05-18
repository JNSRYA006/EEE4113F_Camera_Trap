# Main function that runs on startup of base station

import main_images, main_sense

# could pass in interval for sensor collection here - nice to have

while True:
    main_sense.main()
    main_images.main()