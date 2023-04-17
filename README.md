# Project-PY4E
This is my very first project after taking Dr. Chuck's Python for Everybody


This project aims to scrape download links from the website provided in the courses, and download the target file for data visualization.
(url: https://vincentarelbundock.github.io/Rdatasets/datasets.html)

Step 1. scrape_links.py
The website contains two types of files for downloading. Since we are aiming for the csv files, this program scrapes all download links for csv files using Beautifulsoup. The result will be a txt file, "to_download.txt", containing every download link in each line.

<img width="1280" alt="Screen Shot 2023-04-17 at 1 26 27 PM" src="https://user-images.githubusercontent.com/128351507/232388614-633cfed9-781a-45f8-a327-5219f984e7a7.png">

Step 2. download_file.py
In this program, download_file function takes two arguments, url and the name you want for the downloaded file; however, the second argument is optional, which will grab the last part of the url to name the file. We will download the target file, "movielens.csv", from the url extracted from the txt file created in step 1.

Step 3. proj_0.py
This program creates a database with sqlite3. The file, "movielens.csv", will be inserted into the table, "movie_lens", with "movie_id" and "user_id" combined as a primary key based on the common sense, which a user could only rate a movie once. As for the second table, "top_1_in_20c", it's the table for storing the data of top 1 movie of each year in the 20th century, which is generated from a sql query within the python code. This table would later be used for generating a bar chart.

Step 4. bar_chart.py
This program uses matplotlib library to create a bar chart showing every top movie of each yaer through 20th century according to the data created in step 3. The visualiztion can be easily shown using Jupyter.
