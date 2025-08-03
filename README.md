# OpenAPI からテストとクライアントコードを自動生成する

## OpenAPI 生成

→ FastAPI で API を実装して openapi.json を出力させる

## テストの自動生成

→ [Schemathesis](https://schemathesis.readthedocs.io/en/stable/) を使う

### 実装例

- CI の設定の例： [.github/workflows/test.yml](.github/workflows/test.yml)
  - 参考：[schemathesis/action: GitHub Action that runs Schemathesis tests](https://github.com/schemathesis/action)
- pytest に統合したテストコードの例：[tests/test_main.py](tests/test_main.py)

### 使ってみて感じた注意点

- int を受け取るメソッドは bool が来ても受け取る（Python では bool は int の subclass なので）が、Schemathesis は 4XX を期待したテストをする
- str を受け取る GET メソッドは FastAPI が `null` や `true` や `0` を文字列にキャストして渡すので 200 として受け取れるが、Schemathesis は 4XX 系を期待したテストをしてくる
- Schemathesis はスキーマに合致するかどうかのテスト（property-based test）なので、「（ドメイン知識に照らして）期待通りの値が返るか」のテストはやはり人が書く必要がある

## クライアントコード自動生成

TypeScript で SPA を書くこととする。

~~Hey API で TypeScript の型定義とクライアントコードを生成する~~

OpenAPI Typescript を使うことにした

[swr-openapi | OpenAPI TypeScript](https://openapi-ts.dev/swr-openapi/)

setup

```sh
npm i swr-openapi openapi-fetch
npm i -D openapi-typescript typescript
```

```sh
cd ./frontend
npx openapi-typescript ./openapi.json -o ./src/lib/api/v1.d.ts
```
