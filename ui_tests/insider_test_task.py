import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class InsiderHomePage(BasePage):
    URL = "https://useinsider.com/"

    def open(self):
        self.driver.get(self.URL)

    def is_page_opened(self):
        self.driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]').click()
        return "#1 Leader in Individualized, Cross-Channel CX — Insider" in self.driver.title


class CareerPage(BasePage):
    def open(self):
        self.driver.find_element(By.LINK_TEXT, "Company").click()
        self.driver.find_element(By.LINK_TEXT, "Careers").click()

    def is_page_opened(self):
        return "Insider Careers" in self.driver.title

    def is_locations_opened(self):
        return self.driver.find_element(By.XPATH, '//h3[contains(text(), "Our Locations")]').is_displayed()

    def is_teams_opened(self):
        return self.driver.find_element(By.XPATH, '//h3[contains(text(), "Find your calling")]').is_displayed()

    def is_life_at_insider_opened(self):
        return self.driver.find_element(By.XPATH, '//h2[contains(text(), "Life at Insider")]').is_displayed()

    def see_all_teams(self):
        all_team = self.driver.find_element(By.XPATH, "//a[starts-with(@class,'btn btn-outline-secondary')]")
        self.driver.implicitly_wait(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", all_team)
        self.driver.execute_script("arguments[0].click();", all_team)

        qa_team = self.driver.find_element(By.XPATH, "//h3[contains(text(), 'Quality Assurance')]")
        self.driver.implicitly_wait(3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", qa_team)
        self.driver.execute_script("arguments[0].click();", qa_team)


class QualityAssuranceJobsPage(BasePage):
    def open(self):
        see_all_qa_jobs = self.driver.find_element(By.LINK_TEXT, "See all QA jobs")
        see_all_qa_jobs.click()

    def filter_jobs(self, location, department):
        time.sleep(3)
        self.driver.find_element(By.ID, "select2-filter-by-department-container").click()
        self.driver.find_element(By.XPATH, f"//li[text()='{department}']").click()

        self.driver.find_element(By.ID,"select2-filter-by-location-container").click()
        self.driver.find_element(By.XPATH, f"//li[text()='{location}']").click()

    def are_jobs_list_present(self):
        return len(self.driver.find_elements(By.ID, "jobs-list")) > 0

    def apply_for_job(self):
        time.sleep(3)
        view_role = self.driver.find_element(By.XPATH, "//a[contains(text(), 'View Role')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", view_role)
        self.driver.execute_script("arguments[0].click();", view_role)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return 'jobs.lever.co' in self.driver.current_url


def take_screenshot(driver, step_name):
    screenshot_folder = "screenshots"
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    screenshot_file = os.path.join(screenshot_folder, f"{step_name}.png")
    driver.save_screenshot(screenshot_file)


def run_test(browser_name):
    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")

    try:
        home_page = InsiderHomePage(driver)
        home_page.open()
        assert home_page.is_page_opened(), "Insider home page not opened."
        print("Test #1 passed - Insider home page opened")

        career_page = CareerPage(driver)
        career_page.open()
        assert career_page.is_page_opened(), "Career page not opened."
        print("Test #2 passed - Career page opened.")
        assert career_page.is_locations_opened(), "Locations block not opened."
        print("Test #3 passed - Locations block opened.")
        assert career_page.is_teams_opened(), "Teams block not opened."
        print("Test #4 passed - Teams block opened.")
        assert career_page.is_life_at_insider_opened(), "Life at Insider block not opened."
        print("Test #5 passed - Life at Insider block opened.")

        career_page.see_all_teams()

        qa_jobs_page = QualityAssuranceJobsPage(driver)
        qa_jobs_page.open()
        qa_jobs_page.filter_jobs(department="Quality Assurance", location="Istanbul, Turkey")
        assert qa_jobs_page.are_jobs_list_present(), "No QA jobs found for the specified location and department."
        print("Test #6 passed - QA jobs found for the specified location and department.")

        assert qa_jobs_page.apply_for_job(), "Application form page not opened."
        print("Test #6 passed - Application form page opened.")

    except AssertionError as e:
        take_screenshot(driver, f"{str(e)} - test_failure")
        print(f"Test failed: {str(e)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    run_test("chrome")
