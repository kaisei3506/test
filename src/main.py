import torch
import numpy as np

def main():
    print("Hello from Docker COntainer!")
    print(f"PyTorch version: {torch.__version__}")
    a = np.array([1, 2, 3])
    print(f"Numpy array: {a}")
    print("ローカルでコードを編集しました！")

if __name__ == "__main__":
    main()