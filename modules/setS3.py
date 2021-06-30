import json
from minio import Minio
from io import BytesIO

#  funtion para envio de notificação ao S3
def setS3(notification):

    client = Minio("s3.amazonaws.com", "ACCESS-KEY", "SECRET-KEY")
    notif = json.loads(notification)

    # envio de dado no formato de metadados
    client.put_object(
        "serviceb", str(notif["id"]), BytesIO(b"serviceb"), 5,
        metadata=notif,
    )






