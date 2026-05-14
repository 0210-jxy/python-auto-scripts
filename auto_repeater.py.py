import pyautogui
import time
#设置重复执行次数
loop_times = 5
print("脚本开始执行，请将光标在3秒内移到输入框。")
time.sleep(3)
# 循环执行
for i in range(loop_times):
    print(f"正在执行第 {i+1} 次")

    time.sleep(1)
    pyautogui.typewrite("test")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")

print("✅ 全部执行完成！")