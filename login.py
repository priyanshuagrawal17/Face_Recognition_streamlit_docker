import streamlit as st

import image
from db import Database
import csv 
from datetime import datetime 


def login():
    picture = st.camera_input("picture",key = "registercam", label_visibility='hidden')

    if picture:
        unknown_user_dir = "./unknown_user/"
        unknown_user_name = "unknown_user"
        image.save_image(picture, unknown_user_dir, unknown_user_name)

        is_match, user_id = image.compare_faces_in_directory("./known_user/", unknown_user_dir)

        if is_match:
            db = Database()
            st.write(user_id)
            user_detail = db.get_user_detail(user_id)
            st.write(user_detail.__dict__)
            # Write to CSV on successful login
            log_login(user_id , user_detail)
        else:
            st.error("No Match Found")

        image.delete_image(unknown_user_dir + unknown_user_name)
def log_login(user_id, user_detail):
    # Define the filename for the CSV file
    filename = 'login_records.csv'
    
    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare the data to be written: [timestamp, user_id]
    data = [timestamp, user_id, user_detail.name]
    
    # Open the file in append mode ('a') and write the data
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)