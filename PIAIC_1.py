import torch
import numpy as np
import pandas as pd

from torchvision import datasets
import torchvision.transforms as transform
from torch.utils.data.sampler import SubsetRandomSampler

print ("Hello World")
print ("Noman Tanveer")
print ("Really Nigga")
print ("This is what you're asking me to do?")
print ("This is a good start")
print ("I guess??!!")

transform = transform.Compose([
					transform.Resize(225),
					transform.CenterCrop(224),
					transform.ToTensor(),
					transform.Normalize(0.5, 0.5, 0.5)
					])
					
dict = [ 55, 34, 65, 98]
print (dict)

for ele in dict:
	print (str(ele)+"1")
	
print ("primitive, datatypes, predefined functions")
