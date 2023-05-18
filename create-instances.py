import boto3
from botocore.config import Config
import sys


config = Config(region_name='us-east-1')
ec2 = boto3.resource('ec2', config=config)
cnet_id = "kairongzhang"
ami = 'ami-06a36e005775b6e11'
ending = sys.argv[1]
instances = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=ami,
    InstanceType='t2.nano',
    IamInstanceProfile={
        'Name': 'instance_profile_' + cnet_id
    },
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{
            'Key': 'Name', 'Value': cnet_id + ending
        }]
    }],
        KeyName=cnet_id,
        SecurityGroups=['mpcs-cc']
)
instance = instances[0]

print(instance.id)
print(instance.public_dns_name)