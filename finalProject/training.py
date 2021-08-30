import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

import torch
import torch.nn as nn 
from torch.utils.data import Dataset, DataLoader

from model import NeuralNetwork

with open('intents.json', 'r') as fhand:
  intents = json.load(fhand)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
  tag = intent['tag']
  tags.append(tag)
  for pattern in intent['patterns']:
    word = tokenize(pattern)
    all_words.extend(word)
    xy.append((word, tag))

ignore = ['?', '!', '.', ',']
all_words = [stem(word) for word in all_words if word not in ignore]
all_words = sorted(set(all_words))
tags = sorted(set(tags))


# Put bag of words in here
x_train = []
y_train = []
for (pattern_sentence, tag) in xy:
  bag = bag_of_words(pattern_sentence, all_words)
  x_train.append(bag)

  label = tags.index(tag)
  y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
  def __init__(self):
    self.n_samples = len(x_train)
    self.x_data = x_train
    self.y_data = y_train
  
  # Dataset[index]
  def __getitem__(self, index):
    return self.x_data[index], self.y_data[index]
  
  def __len__(self):
    return self.n_samples

# Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=2)

device = torch.device('cpu')
model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
  for (words, labels) in train_loader:
    words = words.to(device)
    labels = labels.to(device)

    # Forward
    outputs = model(words)
    loss = criterion(outputs, labels)

    # Backward and optimizer step
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  if (epoch+1) % 100 == 0:
    print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')



data = {
  'model_state': model.state_dict(),
  'input_size': input_size,
  'output_size': output_size,
  'hidden_size': hidden_size,
  'all_words': all_words,
  'tags': tags
}

file = 'data.pth'
torch.save(data, file)

print(f'Training complete. File saved to {file}')