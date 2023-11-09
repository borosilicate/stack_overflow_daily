#Stack Overflow Automatic Daily Check-in!

Are you struggling to remember to login to stack overflow every day?!
Would you prefer to not answer strangers coding questions on holidays?
Do you still want to get badges for consistently logging in?

This is the project for you!

Key steps...
1. Have a raspberry pi or other linux server with systemctl.
2. Login to stackoverflow on the device.
3. Change the line in the stack_overflow_daily.py script to your own 
chrome profile.
You can find it by going to chrome://version in your browser.
Replace my path with the profile path.
4. Make sure to install the correct libraries.
sudo apt install chromedriver
pip install selenium
pip install PyVirtualDisplay


