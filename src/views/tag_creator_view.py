from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    ''' Responsable for interacting with HTTP. '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()
        body = http_request.body
        product_code = body["product_code"]

        # Lógica de regra de negócio
        formatted_reponse = tag_creator_controller.create(product_code)

        # Retorno http
        return HttpResponse(status_code=200, body=formatted_reponse)
