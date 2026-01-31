"""
====================================================
ALL-IN-ONE WEB SCRAPING ASSIGNMENT
Tasks:
1. Weather HTML parsing (BeautifulSoup)
2. Job scraping + SQLite + CSV export
3. Laptop scraping from Demoblaze (Selenium) -> JSON
====================================================
"""

# =========================
# COMMON IMPORTS
# =========================
from bs4 import BeautifulSoup
import requests
import sqlite3
import csv
import json
import time

# Selenium imports (Task 3)
from selenium import webdriver
from selenium.webdriver.common.by import By


# ==================================================
# TASK 1: WEATHER HTML SCRAPING
# ==================================================
def task1_weather_scraping():
    print("\n=== TASK 1: WEATHER FORECAST ===")

    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    rows = soup.find("tbody").find_all("tr")
    weather_data = []

    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text.strip()
        temp = int(cols[1].text.replace("°C", ""))
        condition = cols[2].text.strip()

        weather_data.append({
            "day": day,
            "temperature": temp,
            "condition": condition
        })

    # Display weather data
    for data in weather_data:
        print(f"{data['day']}: {data['temperature']}°C, {data['condition']}")

    # Highest temperature
    max_temp = max(d["temperature"] for d in weather_data)
    hottest_days = [d["day"] for d in weather_data if d["temperature"] == max_temp]

    print(f"\nHighest Temperature: {max_temp}°C on {', '.join(hottest_days)}")

    # Sunny days
    sunny_days = [d["day"] for d in weather_data if d["condition"] == "Sunny"]
    print("Sunny Days:", ", ".join(sunny_days))

    # Average temperature
    avg_temp = sum(d["temperature"] for d in weather_data) / len(weather_data)
    print(f"Average Temperature: {avg_temp:.2f}°C")


# ==================================================
# TASK 2: JOB SCRAPING + SQLITE + CSV
# ==================================================
def task2_job_scraping():
    print("\n=== TASK 2: JOB SCRAPING ===")

    URL = "https://realpython.github.io/fake-jobs"
    DB_NAME = "jobs.db"

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        UNIQUE(title, company, location)
    )
    """)

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        apply_link = job.find("a")["href"]

        cursor.execute("""
            SELECT description, apply_link FROM jobs
            WHERE title=? AND company=? AND location=?
        """, (title, company, location))

        existing = cursor.fetchone()

        if existing:
            if existing[0] != description or existing[1] != apply_link:
                cursor.execute("""
                    UPDATE jobs
                    SET description=?, apply_link=?
                    WHERE title=? AND company=? AND location=?
                """, (description, apply_link, title, company, location))
        else:
            cursor.execute("""
                INSERT INTO jobs (title, company, location, description, apply_link)
                VALUES (?, ?, ?, ?, ?)
            """, (title, company, location, description, apply_link))

    conn.commit()

    # Filtering function
    def filter_jobs(location=None, company=None):
        query = "SELECT * FROM jobs WHERE 1=1"
        params = []

        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")

        if company:
            query += " AND company LIKE ?"
            params.append(f"%{company}%")

        cursor.execute(query, params)
        return cursor.fetchall()

    # Export to CSV
    def export_to_csv(filename, jobs):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
            for job in jobs:
                writer.writerow(job[1:])

    filtered_jobs = filter_jobs(location="Remote")
    export_to_csv("filtered_jobs.csv", filtered_jobs)

    conn.close()
    print("Jobs scraped, database updated, CSV exported.")


# ==================================================
# TASK 3: DEMOBLAZE LAPTOP SCRAPING (SELENIUM)
# ==================================================
def task3_laptop_scraping():
    print("\n=== TASK 3: LAPTOP SCRAPING ===")

    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)

    # Click Laptops category
    driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(3)

    # Click Next page
    driver.find_element(By.ID, "next2").click()
    time.sleep(3)

    laptops = []
    cards = driver.find_elements(By.CLASS_NAME, "card-block")

    for card in cards:
        name = card.find_element(By.TAG_NAME, "h4").text
        price = card.find_element(By.TAG_NAME, "h5").text
        description = card.find_element(By.TAG_NAME, "p").text

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    driver.quit()

    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)

    print("Laptop data saved to laptops.json")


# ==================================================
# MAIN EXECUTION
# ==================================================
if __name__ == "__main__":
    task1_weather_scraping()
    task2_job_scraping()
    task3_laptop_scraping()
