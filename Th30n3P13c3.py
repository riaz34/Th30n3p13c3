import requests
import socket 
import threading
import asyncio
from time import sleep
from playwright.async_api import async_playwright

print("""\n1) Port scan
2) Ssl check
3) Security miscon
4) Directory traversal
5) Reflected xss
6) Exit \n""")

while True:

 number = int (input("enter the number: "))

 if number == 1 :
  try:
   url= input("Enter the url: ")

   def port_scanner(port):

      try:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((url, port))
          print(f"Open port => {port}")  

      except:
          pass


   for port in range(0,65535):  

     thread = threading.Thread(target =port_scanner, args=[port]) 
     thread.start() 

  except RuntimeError:
    pass   

 elif number == 2 :
  import requests 

  url=input("Enter the url: ")
  ht="https://"
  url1=ht+url

  try:
      response = requests.get(url1, verify=True)
      print("Ssl certified")

  except requests.exceptions.SSLError:
      print("Ssl not certified")

 elif number == 3 :
  
  print("\nexample url : https://www.google.com/\n")

  url = input("Enter the url: ")
  domain = url

  file = open("config.txt")

  content = file.read()

  directories = content.splitlines()

  counter = 0


  for cfile in directories:

      response = requests.get(f"{domain}{cfile}")
      url = f"{domain}{cfile}"

      if response.status_code == 200:
        print("Security misconfiguration found!",url)
        counter = counter+1
       
      else:
       
        pass
  if counter == 0:
    print("Security misconfiguration not found")
  else:
    pass

 elif number == 4 :

  print("\nexample url : https://insecure-website.com/loadImage?filename=\n")
  
  counter1=0
  url = input("Enter the url: ")
  urld = url

  file = open("dirt.txt")

  contents = file.read()

  directoriesT = contents.splitlines()


  for cfile in directoriesT:

      response = requests.get(f"{urld}{cfile}")
      url = f"{urld}{cfile}"

      if response.status_code == 200:
        print("Directory traversal found!",url)
       
        counter1=counter1+1
       
      else:
       
        pass
  
  if counter1 == 0:
    print("Directory traversal not found")
  else:
    pass

 elif number == 5 :
  urls = input("Enter the url: ")
  async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto(urls)
    sleep(1)

    try:
        await page.wait_for_selector("input[class]")
        await page.type("input[class]", "Su1fur1cAc1d")
    except:
        await page.wait_for_selector("input[type='text']")
        await page.type("input[type='text']", "Su1fur1cAc1d")
    

    sleep(3)
    await page.keyboard.press('Enter')
    sleep(2)
    text_arr =await page.locator("//*[contains(text(),'Su1fur1cAc1d')]").all_text_contents()
    textlen=len(text_arr)
    if textlen>1:
      print("might be vulnerable")
    else:
      print("Not vulnerable")
    
    sleep(2)
    await browser.close()

  async def main():
    async with async_playwright() as playwright:
        await run(playwright)
        
  asyncio.run(main())

  
 elif number == 6:
  break   
  
 else:
   print("\n please select the right number")

