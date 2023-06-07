# ---------------------------------------------------
# Written by liu lulu (liu_lulu@buaa.edu)
# 这段代码还未经过实际应用测试，有实际场景时再进行调试！
# ---------------------------------------------------

import torch
import torch.nn as nn
import torchvision.models as models
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

# 加载预训练的 ResNet-18 模型
resnet = models.resnet18(pretrained=True)
# 移除最后一层全连接层
resnet = nn.Sequential(*list(resnet.children())[:-1])
# 将模型设置为评估模式
resnet.eval()

# 加载图像并进行预处理
image = Image.open('image.jpg')
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)

# 使用 ResNet-18 模型提取特征
with torch.no_grad():
    features = resnet(input_batch)

# 将特征图转换为二维数组
features = features.reshape(features.shape[0], -1)

# 使用 T-SNE 进行降维
# ---------------------------------------------------
'''
`tsne.fit_transform(features)` 中的 `features` 应该是一个二维数组，其维度为 `(n_samples, n_features)`，其中 `n_samples` 是样本数量，`n_features` 是特征数量。

在上述代码中，我们使用 ResNet-18 模型提取的特征图是一个三维张量，具有 `(n_channels, height, width)` 的维度。为了将其作为 T-SNE 的输入，我们需要将其转换为二维数组，形状为 `(n_samples, n_features)`。
'''
# ---------------------------------------------------
tsne = TSNE(n_components=2, random_state=0)
features_tsne = tsne.fit_transform(features)

# 绘制可视化结果
plt.scatter(features_tsne[:, 0], features_tsne[:, 1])
plt.title('T-SNE Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
