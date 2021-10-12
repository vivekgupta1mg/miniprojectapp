TORTOISE_ORM = {
    "connections": {"default": "postgres://so:so123@localhost:5432/sodb"},

    "apps": {
        "sanic_3": {
            "models": [
                "models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}
