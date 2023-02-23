import pyautogui as pg
import time

# to prevent pyautogui from closing by moving the cursor to the 0,0 (corner of the screen)
pg.FAILSAFE = True
pg.PAUSE = 0.5

print('This is a 32 inch curve screen: ', pg.size())


# important:  make sure to open, maximize and close Chrome before starting

# right click Chrome icon on the taskbar
pg.leftClick(515, 1260, 1, 3)
time.sleep(1)


# go to Lee Vision website

def GotoLV():
    pg.leftClick(250, 50, 1, 3)
    pg.write('https://www.leevisionfamilyeyeclinic.com/')
    pg.press('enter')
    time.sleep(1)


# scroll to the top links and verify the titles

def GoToTopLinks():
    pg.moveTo(890,180,2)   
    pg.alert('Lee Vision Family Eye Clinic')

    pg.moveTo(1275,180,2)
    pg.alert('Hours and Location')

    pg.moveTo(1400,180,2)
    pg.alert('The Staff')

    pg.moveTo(1520,180,2)
    pg.alert('Insurance')

    pg.moveTo(1645,180,2)
    pg.alert('Your Eye Health')


# scroll down the left column of links

def GoToLeftLinks():
    pg.moveTo(910,695,2)  
    pg.alert('Schedule an Appointment')

    pg.moveTo(910,750,2)  
    pg.alert('Patient History Form')

    pg.moveTo(910,790,2)  
    pg.alert('Satisfaction Survey')

    pg.moveTo(910,830,2)  
    pg.alert('Order Contacts')

    pg.moveTo(910,885,2)  
    pg.alert('Contact Form')

    pg.moveTo(910,940,2)  
    pg.alert('Read Our Reviews')

    pg.moveTo(930,995,2)  
    pg.alert('Follow Us On FaceBook')
    pg.moveTo(960,995,2)  
    pg.alert('Google Maps')


# header links

def GoToHeaderLinks():
    pg.moveTo(820,90,2)  
    pg.alert('Our Phone Number')

    pg.moveTo(910,90,2) 
    pg.alert('Google Maps')

    pg.moveTo(1335,90,2)  
    pg.alert('Home')

    pg.moveTo(1400,90,2) 
    pg.alert('Contact Us')

    pg.moveTo(1475,90,2)  
    pg.alert('What\'s New')

    pg.moveTo(1565,90,2) 
    pg.alert('Privacy Policy')

    pg.moveTo(1650,90,2)  
    pg.alert('Disclaimer')

    pg.moveTo(1720,90,2) 
    pg.alert('Follow Us On FaceBook')

    pg.moveTo(1755,90,2)  
    pg.alert('Google Maps')


# scroll to the footer links

def ScrollToBottom():
    pg.scroll(-3200)

# footer links

def GoToFooterLinks():
    pg.moveTo(815,1030,2)  
    pg.alert('Our Eye Care Clinic')

    pg.moveTo(930,1030,2)  
    pg.alert('Our Eye Doctor')

    pg.moveTo(1045,1030,2)  
    pg.alert('Eye Care Services')

    pg.moveTo(1175,1030,2)  
    pg.alert('Eyeglasses and Contacts')

    time.sleep(1)

# close Chrome
def CloseChrome():
    pg.leftClick(2535, 15, 1, 3)

######################################################################################
# Status as of 02/19/23:
#
# Links are all verified.
# Next, follow each link and verify the titles.
#
######################################################################################

if __name__ == '__main__':
    GotoLV()
    GoToTopLinks()
    GoToHeaderLinks()
    GoToLeftLinks()
    ScrollToBottom()
    GoToFooterLinks()
    CloseChrome()

