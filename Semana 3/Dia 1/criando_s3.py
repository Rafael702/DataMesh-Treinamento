import boto3
import boto3.s3.connection

access_key = 'ASIA3TQZ6BA26T4VQTP7'
secret_key = 'YyAg4UUm1kEKPAksLy7YqJTwZaPXjqyCftzcQXm0'

#Bucket Connection
conn = boto3.connect_s3(
    aws_access_key_id= access_key,
    aws_secret_access_key= secret_key
)

#Listing all buckets

for bucket in conn.get_all_buckets():
    print("{name}\t{created}".format(
        name = bucket.name,
        created = bucket.creation_date,
    ))

#Creating a Bucket
bucket1 = conn.create_bucket('rafshand1')

#Getting the bucket object
bucket2 = conn.get_bucket('rafshand1')

#Deleting Object in a bucket
bucket2.delete_key('teste2.csv')