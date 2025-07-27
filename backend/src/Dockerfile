# ベースイメージはLambda用ではない通常のものを使う
FROM python:3.12-slim

# Lambda Web Adapterをコピー
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.9.1 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task

# FastAPIで使うポートの設定
ENV PORT=8000

# ライブラリのインストール
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

# ソースコードのコピー
COPY . ./

# uvicornサーバーの起動（main:app はmain.pyにappというFastAPIのインスタンスがあることを想定している）
CMD ["sh", "-c", "exec uvicorn --port=$PORT main:app"]