# LeavesCalculator v.1.0.1
This is the repository for a web app that is designed for Portland State University's HR department
to assist PSU employees with determining the amount and types of leave they are eligible for. This forked 
version has been modified from the original to run as 2 docker containers, one for the Vue.js frontend
and one for the Django backend.

This app uses Django, REST, Vue.js, NPM, and SQLite3 frameworks, and is released under MIT license.

## Getting Started - The Quick Method
Follow these instructions if you just want to get the app running quickly and easily:
1. Docker will be required, download it here: https://docs.docker.com/get-docker/
2. In your terminal, type the following two commands sequentially (they will pull the application
down from the docker hub and run them in the background of your terminal):
<br>`sudo docker run -d averyscottnorris/leavesappdjango`
<br>`sudo docker run -d averyscottnorris/leavesappvue`
3. Open your web browser and navigate to localhost:8080
4. And that's it! See the "Using the App" section below for more information about using the application
5. Use `sudo docker ps` to view running containers, and `sudo docker stop [CONTAINER_ID]` to stop each container

## Getting Started - Cloning the project
If you want to make modifications to the project, follow these steps:
1. Docker will be required, download it here: https://docs.docker.com/get-docker/ 
2. Docker-compose will be required (may be bundled with docker): https://docs.docker.com/compose/install/
3. Change directory to where you want the LeavesCalculator directory to be created
4. Run:g `git clone https://github.com/averyscottnorris/LeavesCalculator.git`
5. Make modifications to the code as desired, and rebuild and run the images with the command: `sudo docker-compose up`
6. The application is now running! Open your web browser and navigate to localhost:8080 to view the app
7. Use `sudo docker-compose down` to spin the containers back down when finished.

## Using the App
Now that the app's running, you can play around with it!
1. Login as a user to walk through the question graph (user: adent pass: 1234)
2. Login as admin (user: admin pass: 1234) and use the "Admin" tab to modify the question flow graph

## NOTES
1. Remember to change the Django "SECRET_KEY" in LeavesAppBE/settings.py