1. Label more data and update the model.
2. Work on that line thing to count how many vehicles have passed from one point to another point.
3. Dockerize the whole application for submission.
    a. If its a turning patterns problem then we should have an app.py file which will accept input like this: python app.py Stn_HD_1.mp4 Output_Turning_Patterns.csv
    b. If the task is to provide short-term (e.g., 30 minutes into the future) predictions of the vehicle counts (by vehicle type), then we have to run the model through all the videos that they have given and then should be able to forecast the number of vehicles.
