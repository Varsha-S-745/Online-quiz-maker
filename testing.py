from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pyhtmlreport import Report

report = Report()
report.setup(report_name="Online Quiz Maker - Selenium Test Report", output_path=".")

driver = webdriver.Chrome()  
driver.maximize_window()

try:
    with report.step("Signup Test"):
        driver.get("http://localhost:3000/signup") 
time.sleep(1)
        driver.find_element(By.NAME, "username").send_keys("testuser")
        driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        report.log("Signup test executed successfully", status="pass")

    with report.step("Login Test"):
        driver.get("http://localhost:3000/login")  
        driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
report.log("Login test run successfully", status="pass")

    with report.step("Create Exam Test"):
        driver.get("http://localhost:3000/create-exam") 
        driver.find_element(By.NAME, "exam_title").send_keys("Python Basics Quiz")
        driver.find_element(By.NAME, "add_question").click()
driver.find_element(By.NAME, "question_1").send_keys("What is Python?")
        driver.find_element(By.NAME, "option_1a").send_keys("A programming language")
        driver.find_element(By.NAME, "option_1b").send_keys("A snake")
        driver.find_element(By.NAME, "correct_answer_1").send_keys("A programming language")
        driver.find_element(By.NAME, "submit_exam").click()
        time.sleep(2)
report.log("Create Exam test run successfully", status="pass")

    with report.step("Attempt Exam Test"):
        driver.get("http://localhost:3000/exams")
        driver.find_element(By.LINK_TEXT, "Python Basics Quiz").click()
        driver.find_element(By.NAME, "answer_1").click()  # Choose correct answer
driver.find_element(By.NAME, "submit").click()
        time.sleep(2)
        report.log("Attempt Exam test executed successfully", status="pass")

    with report.step("Grade Exam Test"):
        driver.get("http://localhost:3000/results") 
        score = driver.find_element(By.ID, "score").text
        report.log(f"Score shown: {score}", status="pass")

except Exception as e:
    report.log(f"Test failed because of: {str(e)}", status="fail")

finally:
    driver.quit()
    report.generate()
