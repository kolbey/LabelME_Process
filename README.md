# LabelME_Process

### 使用 LabelME 标注进行语义分割数据标注

### 操作步骤：

> 1. LabelME标注后生成JSON标注文件
> 2. 使用json_label.py生成mask图像
> 3. 使用find_copy_images.py将上一步的mask命名为对应image的名称，并复制到数据集的lables目录内
> 4. 使用resize_rename_images.py将原始image与最终的mask重命名，并调整为训练所需的大小
> 5. 完成上述步骤即可，得到XX数据集内的images目录（存放图像）与labels目录（存放标签）