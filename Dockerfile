# ベースライン
# python:3.11-slimはただ「Python 3.11を使う」という意味だけでなく「Docker Hubで公開されているpython:3.11-slimという名前の完成済みベースイメージを土台にする」という意味
# python:3.11-slimイメージは、非常に人気があり安定しているLinuxディストリビューションであるDebianをベースにしている
FROM python:3.11-slim

# 環境変数と作業ディレクトリ
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# pipを使ってuvをインストール
RUN pip install uv

# requirements.txtをコピーする
COPY requirements-base.txt .

# uvを使ってライブラリをインストール
# --mount=type=cacheを使うことでuvのキャッシュをビルド間で共有し、
# 2回目以降のビルドを劇的に高速化
RUN --mount=type=cache,target=/root/.cache/uv uv pip install --system -r requirements-base.txt

# 頻繁に変わる軽いライブラリをインストール
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/uv uv pip install --system -r requirements.txt

# プロジェクトのコードをコピーする
COPY . .