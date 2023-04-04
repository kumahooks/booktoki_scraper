# As far as I'm aware, as of 4th of april 2023, this doesn't work anymore in booktoki169.com

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

url = "https://booktoki169.com/novel/1756437"

driver = webdriver.Firefox()
driver.get(url)

# Button for the next chapter
go_next = "//*[@id=\"goNextBtn\"]"

# Container where the chapter text is
novel_div = "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[2]/section/article/div[3]/div[2]"

while (True):
	while (True):
		if (go_next_find := driver.find_elements(By.XPATH, go_next)) is not None:
			break

	while (True):
		if (novel_div_find := driver.find_elements(By.XPATH, novel_div)) is not None:
			break

	file_path = os.path.join("raws", f"{driver.title}.txt")
	with open(file_path, "w") as file:
		raw_text = novel_div_find[0].get_attribute('innerHTML')
		# Because we gather the div's innerHTML there will be a bunch of stuff that we need to clean
		raw_text = raw_text.replace("<p>", "").replace("</p>", "").replace("<div>", "").replace("</div>", "").replace("<br>", "\n")
		file.write(raw_text)

	file.close()

	go_next_find[0].click()

driver.close()
