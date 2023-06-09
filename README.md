# ToolBox

### LabelME 语义分割数据标注

#### 具体操作步骤：

> 1. LabelME标注后生成JSON标注文件
> 2. 使用json_label.py生成mask图像
> 3. 使用find_copy_images.py将上一步的mask命名为对应image的名称，并复制到数据集的lables目录内
> 4. 使用resize_rename_images.py将原始image与最终的mask重命名，并调整为训练所需的大小
> 5. 完成上述步骤即可，得到XX数据集内的images目录（存放图像）与labels目录（存放标签）

### 其他图像后处理及常用工具：

#### **overlay_mask_on_image.py** 

- 用来将语义分割模型预测的mask与原始输入图像image叠加在一起，形成更加直观的可视化效果。

#### **write_file_path_to_txt.py** 

- 用来将训练数据集中的image图像和mask标签的目录写入一个txt文件中，满足部分训练框架只能从txt文件加载训练的需求。

#### **feature_map_tsne_visualation.py** 

- 用来将深层特征图进行可视化，形成特征信息降维后的二维分布图。

#### **screenshot.py** 
- 该程序是一个示例程序，可以通过`pyautogui`监控屏幕，捕获屏幕的画面内容。

#### **capture_test.py** 
- 该程序是一个示例程序，可以通过`cv2.VideoCapture`读取指定摄像头或视频文件的内容，并将视频播放在指定大小的窗口中。

#### **socket_connect.py** 
- 该程序是一个示例程序，示例通过`socket`实现不同主机之间的通信，其中已经实现客户端与服务器双向通信，以及客户端与服务器双向持续通信的功能。