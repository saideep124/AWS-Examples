import boto3
import json
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    volume_id = event.get('volume_id')
    current_date = datetime.now().strftime("%Y-%m-%d")

    if not volume_id:
        return {"statusCode": 400,
                "body": json.dumps("No Volume ID provided")
                }
    snapshot_id=None
    try:
        response=ec2.snapshot(VolumeId=volume_id,description=f"{current_date} -  Lambda Snapshot of {volume_id}")
        snapshot_id = response["SnapshotId"]
    except Exception as e:
        return {"statusCode": 500,}


    ec2.createTags(Resources=[snapshot_id],Tags=[{"Key":"Name","Value":snapshot_id},{"Key":"created","Value":"Lambda Snapshot Created"}])


    return {
        "statusCode": 200,
        "body":{
            "message": "Snapshot Created successfully",
            "snapshot_id":snapshot_id,
        }
    }


