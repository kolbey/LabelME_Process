import cv2
import pyautogui
import numpy as np

# 获取屏幕尺寸
screen_size = (1920, 1080)  # 替换为您的屏幕分辨率

# 创建窗口
cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)

# 循环读取和显示屏幕画面
while True:
    # 截取屏幕画面
    screenshot = pyautogui.screenshot()
    
    # 将截图转换为 OpenCV 图像格式
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 显示屏幕画面
    cv2.imshow("Screen Capture", frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 关闭窗口
cv2.destroyAllWindows()
