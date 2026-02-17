device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

import torch

x = torch.rand(10000, 10000).cuda()
y = torch.rand(10000, 10000).cuda()
z = torch.matmul(x, y)

print(z)
