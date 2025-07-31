# Frontend SPA APP

- app: React + TypeScript + Vite
- hosting: Amplify Hosting
- client: [openapi-ts](https://heyapi.dev/openapi-ts/get-started)

## client の生成

FastAPI の dev サーバーを立てた状態で次のコマンドを打てばよい

```sh
$ npm run gen-client

> frontend@0.0.0 gen-client
> openapi-ts

⏳ Generating from http://127.0.0.1:8000/openapi.json
🚀 Done! Your output is in ./src/client
```

なぜうまくいくのか？

- `package.json` にコマンドのエイリアスを入れてある
- `openapi-ts.config.ts` に FastAPI の openapi.json の URL を設定している
