import requests
import os
from bs4 import BeautifulSoup
import time
import yagmail
import logging


URL_TO_MONITOR = "http://hacker-festzelt.de/reservierung/"
DELAY_TIME = 300 # seconds aka 5 minutes

SENDING_EMAIL_USERNAME = "yourgmail@gmail.com" 
SENDING_EMAIL_PASSWORD = "yourpassword"
RECIPIENT_EMAIL_ADDRESS = [
    "yourmail@mail.com",
    "yoursecondmail@mail.com"]


#! Check Wephbpage for changes
def process_html(string):
    soup = BeautifulSoup(string, features="lxml")
    # make the html look good
    soup.prettify()
    # remove script tags
    for s in soup.select('script'):
        s.extract()
    # remove meta tags 
    for s in soup.select('meta'):
        s.extract()
    # convert to a string, remove '\r', and return
    return str(soup).replace('\r', '')

def webpage_was_changed(): 
    """Returns true if the webpage was changed, otherwise false."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(URL_TO_MONITOR, headers=headers)

    if not os.path.exists("previous_content.html"):
        open("previous_content.html", 'w+').close()
    
    filehandle = open("previous_content.html", 'r')
    previous_response_html = filehandle.read() 
    filehandle.close()

    processed_response_html = process_html(response.text)

    if processed_response_html == previous_response_html:
        return False
    else:
        filehandle = open("previous_content.html", 'w')
        filehandle.write(processed_response_html)
        filehandle.close()
        return True

#! Send Email Alert
def send_email_alert(alert_str):
    """Sends an email alert. The subject and body will be the same. """
    yagmail.SMTP(SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD).send(
        RECIPIENT_EMAIL_ADDRESS, alert_str, alert_str)

    print("Email sent.")

#! forerver loop
def main():
    log = logging.getLogger(__name__)
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor")

    while True:
        try:
            if webpage_was_changed():
                log.info("WEBPAGE WAS CHANGED.")
                send_email_alert(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!")

            else:
                log.info("Webpage was not changed.")

        except:
            log.info("Error checking website.")

        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    main()
