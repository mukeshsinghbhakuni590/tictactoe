from jsonschema import validate

schema0 = {
            "type" : "object",
            "properties" : {
                "user1" : {"type" : "string"},
                "user2" : {"type" : "string"},
                "token" : {"type" : "string"}
            }
        }

schema1 = {
            "type" : "object",
            "propeties" : {
                "user_id" : {"type" : "string"},
                "gi_id" : {"type" : "string"},
                "token" : {"type" : "string"}
            }
}

def validate_user_ids(payload):
    try:
        validate(payload,schema0)
        return True
    except:
        return False

def validate_game_obj_id(payload):
    try:
        validate(payload,schema1)
        return True
    except:
        return False