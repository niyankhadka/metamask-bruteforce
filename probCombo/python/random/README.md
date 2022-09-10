Random Method

This method is used to generate combinations with random functionality where random keys are taken to create different combinations. This process has probability to create duplication of output as random entities are taken out. 

This script is based on python and fully automation process. Refer to below instructions for more information regarding this method.

Setup Instructions:

Step 1:

r1.py
This file is expanded from the rfunctions.py file. You can create multiple file from rfunctions.py and run simultaneously. For example, you can create multiple r2,r3,r4 and so on. Make sure to copy paste all the codes from r1.py and make few changes.

    dump_file_name = "dump/dump_1.txt"
        Change the dump_1 number to 2,3,4..... as per the file you have created r2,r3,r4.... so that there won't be any conflicts on file name.

    move_file_name = "check/check-1-{}.txt".format(todays_date)
        All you have to change is number as per the file you have created r2,r3,r4....

Use below command to run the file:
    python r1.py
    python r2.py
    ............
    ............

Step 2:

c.py
This file is used to check the valid or invalid generated combinations. Make changes to following variable as per your setup of environment. 

    EXTENSION_PATH: Give directory to crx path of the extension of metamask.

    BINARY_LOCATION: This is optional for other browsers. You can give path to your browser opening file.

    CHROME_DRIVER: As per your browser, download the driver file and save it to resources folder. Then give path to this driver.

    mm_extension_id: Give metamask extension id here.

Make sure to install two library to run this file.

selenium 
    pip install selenium

pyperclip 
    pip install pyperclip

Use below command to run the file:
    python c.py

Note: Before running this file, make sure check folder has at least one file and it will run untill and unless you stop it.

Step 3:

v.py
This file is to check valid combinations to find jackpot combinations. Make changes to following variable as per your setup of environment. 

    EXTENSION_PATH: Give directory to crx path of the extension of metamask.

    BINARY_LOCATION: This is optional for other browsers. You can give path to your browser opening file.

    CHROME_DRIVER: As per your browser, download the driver file and save it to resources folder. Then give path to this driver.

    mm_extension_id: Give metamask extension id here.

Make sure to install two library to run this file.

selenium:
    pip install selenium

pyperclip:
    pip install pyperclip

Use below command to run the file:
    python v.py

Note: Before running this file, make sure check folder has at least one file and it will run untill and unless you stop it. Also, there is one problem with this method, you cannot run two files c.py and v.py at one time on same machine. As copy to clipboard might bring issue on both case, so this one is defect of this method. If you want to use two files on separate machine, then it's fine. 

Alternative:
In above issue, skip Step 2 and 3 and proceed to read below message.
I have joined c.py and v.py on single file called as cv.py where you can run this on same machine. It is combination of two files where you can easily run without any issue. 

cv.py:
As per above inforamtion of file, edit the file as per requirement.

Thankyou.
