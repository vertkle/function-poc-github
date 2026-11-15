import json
import azure.functions as func
from service.function_service import suma

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route("hello", methods=["POST"])
def run_function(req: func.HttpRequest) -> func.HttpResponse:

    print("Init function")
    body = req.get_json()
    num1, num2 = body.values()
    result = suma(num1, num2)

    return func.HttpResponse(
        json.dumps({"data": f"la suma es {result}"}),
        status_code=200,
        mimetype="application/json"
    )