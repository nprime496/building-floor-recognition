class SimpleNet(nn.Module):
    def __init__(self,in_channels=1,n_output=3):
        super().__init__()
        self.network = nn.Sequential(
            
            nn.Conv2d(in_channels, out_channels = 128, kernel_size = 5, padding = 1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 64, kernel_size = 5, stride = 1, padding = 1),
            nn.BatchNorm2d(64),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            nn.MaxPool2d(2,2),

        
            nn.Conv2d(64, 32, kernel_size = 3, stride = 1, padding = 1),
            nn.BatchNorm2d(32),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            nn.Conv2d(32,16, kernel_size = 3, stride = 1, padding = 1),
            nn.BatchNorm2d(16),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            nn.MaxPool2d(2,2),
            
            nn.Conv2d(16, 16, kernel_size = 3, stride = 1, padding = 1),
            nn.BatchNorm2d(16),
            nn.Dropout(p=0.2),
            nn.ReLU(),
            # nn.Conv2d(64,64, kernel_size = 3, stride = 1, padding = 1),
            # nn.BatchNorm2d(64),
            # nn.ReLU(),
            nn.MaxPool2d(2,2),

            # nn.Conv2d(64,32, kernel_size = 3, stride = 1, padding = 1),
            # nn.BatchNorm2d(32),
            # nn.ReLU(),
            # nn.MaxPool2d(2,2),

            # nn.Conv2d(128,32, kernel_size = 3, stride = 1, padding = 1),
            # nn.ReLU(),
            # nn.MaxPool2d(2,2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(9072,128),
            nn.ReLU(),
            #nn.Linear(512, 256),
            #nn.ReLU(),
            nn.Linear(128,n_output),
            # nn.Softmax(),
        )
    
    def forward(self, xb):
        emb = self.network(xb)
        return self.classifier(emb)
