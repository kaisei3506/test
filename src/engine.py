import torch
import torch.nn.functional as F


def train(model, x_data, y_data, optimizer, criterion, epochs, device):

    model.to(device)
    x_data = x_data.to(device)
    y_data = y_data.to(device)

    print("Training started...")
    model.train()
    
    for epoch in range(epochs):
        # 勾配をリセット
        optimizer.zero_grad()

        # フォワードパス
        outputs = model(x_data)

        loss = criterion(outputs, y_data)

        loss.backward()

        optimizer.step()

        if (epoch+1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

    print("Training finished...")


def eval_model(model, x_data, y_data):
    print("\nEvaluating model...")
    model.eval()

    with torch.no_grad():
        outputs = model(x_data)
        predicted_probs = torch.sigmoid(outputs)
        predicted_labels = (predicted_probs > 0.5).float()

        accuracy = (predicted_labels == y_data).float().mean()
        print(f'Accuracy on training data: {accuracy.item():.4f}')