from . import gateway


def post_message_to_device(device_id, message):
    """
    Post message to a spark core device
    """
    payload = {
        'message': message,
    }
    gateway.post_message(device_id, payload)

