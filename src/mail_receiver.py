class MailReceiver:
    """Class made to simplify handling mail receivers."""

    def __init__(self, receiver_properties: dict):
        self.name: str = receiver_properties["name"]
        self.mail: str = receiver_properties["mail"]
        self.uuid: str = receiver_properties["uuid"]
