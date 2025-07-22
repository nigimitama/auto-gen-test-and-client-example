# OpenAPI からテストとクライアントコードを自動生成する

## OpenAPI 生成

→ FastAPI で API を実装して openapi.json を出力させる

## テスト自動生成

→ [Schemathesis](https://schemathesis.readthedocs.io/en/stable/) を使う

使ってみて感じた難しさは、str を受け取る GET メソッドは FastAPI が `null` や `true` や `0` を文字列にキャストして渡すので 200 として受け取れるが、Schemathesis は 4XX 系を期待したテストをしてくること。

また、Schemathesis はスキーマに合致するかどうかのテストなので期待通り動作しているかなどのテストはやはり人が書く必要がある

## クライアントコード自動生成

TypeScript で SPA を書くこととする。

Hey API で TypeScript の型定義とクライアントコードを生成する

## CI

[schemathesis/action: GitHub Action that runs Schemathesis tests](https://github.com/schemathesis/action)
