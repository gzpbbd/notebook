import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn, optim
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 前向传播，计算模型的输出
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        # 计算张量x的特征数量
        size = x.size()[1:]
        num_features = 1
        for i in size:
            num_features *= i
        return num_features


if __name__ == '__main__':
    BATCH_SIZE = 32
    GPU_NUM = 0
    NUM = 0
    PATH = './cifar_net.pth'

    # 数据转换器
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    # 获取内置数据
    trainset = torchvision.datasets.CIFAR10(root='~/file_buffer/datasets/CIFAR10', train=True, download=True,
                                            transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
    testset = torchvision.datasets.CIFAR10(root='~/file_buffer/datasets/CIFAR10', train=False, download=True,
                                           transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)
    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    # 获取设备
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(device)

    # 实例化网络，置于GPU上
    net = Net()
    net.to(device)
    print(net)

    # 实例化损失函数、优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.RMSprop(net.parameters(), lr=0.001)

    total_loss = 0
    for epoch in range(2):
        for i, data in enumerate(trainloader):
            # 获取模型输入输出，置于GPU上
            input_datas, labels = data[0].to(device), data[1].to(device)

            # 梯度清零
            optimizer.zero_grad()

            # 前向传播，计算损失，反向传播计算梯度，更新梯度
            output_datas = net(input_datas)
            loss = criterion(output_datas, labels)
            loss.backward()
            optimizer.step()

            # 打印损失
            total_loss += loss.item()
            if i % (10000 // BATCH_SIZE) == 0:
                print('loss {}'.format(total_loss / 2000))
                total_loss = 0

    print('finished training')

    # 保存模型
    torch.save(net.state_dict(), PATH)

    # 加载模型
    net = Net()
    net.load_state_dict(torch.load(PATH))

    # 查看模型精度
    total = 0
    correct = 0
    with torch.no_grad():
        for images, labels in testloader:
            # 前向传播，获取预测的各个类别的energy
            outputs = net(images)
            # 得到预测标签
            _, predicted_labels = torch.max(outputs.data, 1)
            # 统计预测正确的样本数量
            total += images.size()[0]
            correct += (predicted_labels == labels).sum().item()

    print('accuracy of the netword on the 10000 test images: {} %'.format(100 * correct / total))
