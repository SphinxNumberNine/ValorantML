Data Labeling Instructions:

- Follow installation instructions for labelme (https://github.com/wkentaro/labelme)
- In your terminal (mac/linux) or conda env (windows), cd into the project directory `ValorantML\`
- Moses run: `labelme to_label1 --labels labels.txt`
- Humza run: `labelme to_label2 --labels labels.txt`
- The labelme GUI should open up and it should show you the first image in the directory
- Click File->Save Automatically in the top left
- Press `ctrl + r` to enable the rectangle drawing tool
- Click on the top left of the image, then click on the bottom right. A rectangle should appear surrounding the image (might not be perfectly aligned, but it's fine as long as it gets the agent within its bounds)
- In the popup menu that shows up, select the agent that the current picture is showing
- Press `D` to move onto the next image
- Repeat the last 3 steps until all images in the directory are labeled

Immediate Tasks:
- build ultimate classifier
    - crop screenshots to only ults, classify the same way we did for agents
- dot counter for abilities (ASHWATH)
- internal state logic for current "inventory" of abilities
- capturing current round time, starting timer thread when bomb gets planted

Ways Rounds Can End: (investigate later)
- Eliminations (either side)
- Time runs out (t side)
- T side plants, bomb explodes
- T side plants, ct defuses
- T side plants, gets all the kills
