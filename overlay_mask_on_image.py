from PIL import Image
import os

def overlay_masks_on_images(image_directory, mask_directory, save_directory):
    # 遍历图像目录下的所有文件
    for filename in os.listdir(image_directory):
        image_path = os.path.join(image_directory, filename)
        if os.path.isfile(image_path):
            try:
                # 构造相应的掩码文件路径
                mask_filename = filename
                # mask_filename = os.path.splitext(filename)[0] + ".png"
                mask_path = os.path.join(mask_directory, mask_filename)

                # 检查掩码文件是否存在
                if not os.path.isfile(mask_path):
                    print(f"掩码文件不存在: {mask_path}")
                    continue

                # 打开原始图像和掩码图像
                image = Image.open(image_path)
                mask = Image.open(mask_path)

                # 将掩码图像调整为与原始图像相同的大小
                # mask = mask.resize(image.size, resample=Image.BILINEAR)

                # 将掩码图像转换为RGBA模式，使其具有透明度通道
                mask = mask.convert("RGBA")

                # 创建一张新的图像，将原始图像和掩码图像叠加在一起
                overlay = Image.blend(image.convert("RGBA"), mask, 0.3)

                # 构造保存路径
                save_path = os.path.join(save_directory, filename)

                # 保存叠加后的图像
                overlay.save(save_path)
                print(f"已保存叠加图像: {save_path}")

            except Exception as e:
                print(f"处理图像时发生错误: {filename} - {str(e)}")

# 指定原始图像目录、掩码图像目录和保存目录
image_directory = "../../DATASET/RUNWAYS/images/"
mask_directory = "./val_results/"
save_directory = "./overlay/"

# 调用函数进行图像叠加和保存
overlay_masks_on_images(image_directory, mask_directory, save_directory)
