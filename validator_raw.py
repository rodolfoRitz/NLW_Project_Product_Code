from cerberus import Validator

body = {
    "data": {
        "elemento1": 'Eu parei no minuto 25:08!!',
        "elemento2": '45,6',
        "elemento3": '34.5',
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False},
            "elemento2": { "type": "float", "required": True, "empty": False},
            "elemento3": { "type": "float", "required": True, "empty": False}
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print('Body OK')
