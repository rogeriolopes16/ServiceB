import json
from minio import Minio
from io import BytesIO


def setS3(notification):
    # Create client with access and secret key.
    client = Minio("s3.amazonaws.com", "ACCESS-KEY", "SECRET-KEY")
    notif = json.loads(notification)

    # Upload data with metadata.
    client.put_object(
        "serviceb", str(notif["id"]), BytesIO(b"serviceb"), 5,
        metadata=notif,
    )






