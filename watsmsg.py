import pyautogui
import time
txt = str(input("Enter Your Message : "))
msg = int(input("Enter MSG No : "))
c=0
time.sleep(1)
for i in range(1,msg+1):
	print("Sending...",end=" / ")
	time.sleep(0.5)
	pyautogui.typewrite(txt)
	time.sleep(0.5)
	pyautogui.press('enter')
	msg=msg-1
	print("[",i,"] Messege Sent Successfully & ",msg,"Remaining...")
	c=c+1
print("\nTotal {} Messege Sent Successfully".format(c))