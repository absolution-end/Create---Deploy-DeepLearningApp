import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# load model
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork,self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size,num_classes)
        
    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out 
input_size =784 # 28*28
hidden_size=100
num_classes=10
model = NeuralNetwork(input_size, hidden_size, num_classes)

PATH = "mnist_mod.pth"
model.load_state_dict(torch.load(PATH))
model.eval()

# image to tensor
def transform_image(image_bytes):
    transform = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                    transforms.Resize((28,28)),
                                    transforms.ToTensor(),
                                transforms.Normalize((0.1307),(0.3081))]) 
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0).view(-1,28*28)
# predict
def get_prediction(image_tensor):
    # images = image_tensor.reshape()
    output = model(image_tensor)
        
    # value and index
    _, predictions = torch.max(output,1)
    return predictions.item()