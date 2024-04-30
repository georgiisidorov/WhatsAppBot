from selenium.webdriver.common.by import By

from selenium_driver import get_chromedriver


class WebWhatsApp():


	def __init__(self, use_proxy, name):
		self.browser = get_chromedriver(use_proxy=use_proxy, name=name)


	def open(self):
		self.browser.get('https://web.whatsapp.com/')


	def send_message(self, phone, text='', filepath=''):
		self.browser.get(f'https://web.whatsapp.com/send/?phone={phone}&text&type=phone_number&app_absent=0')
		time.sleep(10)
		if text:
			textbox = self.browser.find_element(By.CSS_SELECTOR, "div[tabindex='10']")
			textbox.click()
			textbox.send_keys(text)
			button_send = self.browser.find_element(By.CSS_SELECTOR, "button[data-tab='11']")
			button_send.click()
			time.sleep(3)
		if filepath:
			self.browser.find_element(By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']").click()
			time.sleep(3)
			fileinput = self.browser.find_element(By.CSS_SELECTOR, "input[type='file']")
			fileinput.send_keys(filepath)
			time.sleep(3)
			self.browser.find_element(By.CSS_SELECTOR, "span[data-icon='send']").click()
			time.sleep(5)


	def close(self):
		self.browser.quit()