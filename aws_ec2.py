import boto3

ec2 = boto3.resource('ec2')
instance_name='Segmentation-process-id'
instance_id=None
instances=ec2.instances.all()
instance_exists=False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists=True
            instance_id=instance.id
            print(f'Instance {instance_id}  with name {instance_name}')
            break
    if instance_exists:
        break

if not instance_exists:
    print(f'Instance {instance_id}  with name {instance_name} does not exist')

    # Create EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0abcdef1234567890',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )
    instance_id=instances[0].id
    # Instance object
    instance = instances[0]
    print("Instance ID:", instance.id)

#start Instance
ec2.instance(instance_id).stop()
print("Instance is Stopped")
# Stop Instance
ec2.instance(instance_id).start()
print("Instance is Started")


# Terminate Instance
ec2.instance(instance_id).terminate()
print("Instance is Terminated")





