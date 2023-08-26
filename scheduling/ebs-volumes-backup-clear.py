import boto3
import time

def lambda_handler(event, context):
    client = boto3.client('ec2')

    response = client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': ['available']
            }
        ],
    )

    num_volumes = len(response["Volumes"])
    print(f"Number of available volumes: {num_volumes}")
    
    for volume in response["Volumes"]:
        volume_id = volume["VolumeId"]
        print(f"Processing Volume: {volume_id}")

        # Creating snapshot
        print(f"Creating snapshot for Volume: {volume_id}...")
        client.create_snapshot(VolumeId=volume_id)
        time.sleep(5)

        # Deleting volume
        print(f"Deleting Volume: {volume_id}...")
        client.delete_volume(VolumeId=volume_id)

    return {
        'statusCode': 200,
        'body': f"Processed {num_volumes} available volumes."
    }
