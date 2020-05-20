import pyautogui
import os
import time
import base64
pics = [
"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"
]
#释放资源文件
for p in range(len(pics)):
    imgdata = base64.b64decode(pics[p])
    file = open("step-{}.png".format(str(p+1)),'wb')
    file.write(imgdata)
    file.close()
print("Current position: " + str(pyautogui.position()))
print(pyautogui.size())
time.sleep(2)
#打开安装目录
os.startfile(r"C:\Program Files (x86)\360\360Safe")
time.sleep(1)
#滚动屏幕至目录底部
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
#识别,双击卸载程序
uninstalllocation = pyautogui.locateOnScreen('step-1.png')
#print(uninstalllocation)
uninstallpoint = pyautogui.center(uninstalllocation)
print("uninstall.exe point: " + str(uninstallpoint))
ux,uy = uninstallpoint
pyautogui.click(ux, uy,clicks=2)
time.sleep(3)
#识别,点击卸载按钮
contiune_location = pyautogui.locateOnScreen('step-2.png')
#print(contiune_location)
cotiune_point = pyautogui.center(contiune_location)
print("Step 1-2 point : " + str(cotiune_point))
c1x,c1y = cotiune_point
pyautogui.click(c1x, c1y)
time.sleep(3)
#点击卸载按钮,位置同上
pyautogui.click(c1x, c1y)
time.sleep(3)
#再次确认卸载按钮
contiune_location = pyautogui.locateOnScreen('step-2.png')
#print(contiune_location)
cotiune_point = pyautogui.center(contiune_location)
print("Step 3 point : " + str(cotiune_point))
c3x,c3y = cotiune_point
pyautogui.click(c3x, c3y)
time.sleep(3)
#确认卸载
contiune_location = pyautogui.locateOnScreen('step-3.png')
#print(contiune_location)
cotiune_point = pyautogui.center(contiune_location)
print("Step 4 point : " + str(cotiune_point))
c4x,c4y = cotiune_point
pyautogui.click(c4x, c4y)