import yaml
import torch
import torch.nn as nn
import torch.optim as optim

from .models import MLP
from .engine import train, eval_model
from .utils import set_seed


def main():
    # 設定ファイルの読み込み
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)

    set_seed(config['environment']['seed'])

    if config['environment']['device'] == 'auto':
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    else:
        device = config['environment']['device']

    # 100個の二次元データを作成
    x = torch.randn(config['data']['n_samples'], config['data']['n_features'])
    y = (x[:, 0] + x[:, 1] > 0).float().unsqueeze(1)

    x, y = x.to(device), y.to(device)

    model = MLP(
        input_dim=config['model']['input_dim'], 
        hidden_dim = config['model']['hidden_dim'], 
        output_dim = config['model']['output_dim']
    )
    model.to(device)

    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])

    train(model, x, y, optimizer, criterion, epochs=config['training']['epochs'], device=device)
    eval_model(model, x, y)


if __name__ == "__main__":
    main()