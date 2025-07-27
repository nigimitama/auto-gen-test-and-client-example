import schemathesis

# (1)OpenAPI仕様書のURLを指定してスキーマを生成
schema = schemathesis.openapi.from_url("http://127.0.0.1:8000/openapi.json")

@schema.parametrize()  # (2)スキーマと戦略の定義に基づいてテストケースを生成
def test_api(case):
    """pytestでAPIのテストを実行する関数"""
    # (3)Schemathesisが生成したテストケースを使用してAPIを呼び出し、検証を行う
    case.call_and_validate()
