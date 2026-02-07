import boto3


s3=boto3.resource('s3')
bucket_name='dct-curd-1'

all_my_buckets=[bucket.name for bucket in s3.buckets.all()]
print(all_my_buckets)
is_bucket_created=False

# Bucket Creation
if bucket_name not in all_my_buckets:
    print('Bucket name not found in s3 bucket')
    s3.create_bucket(Bucket=bucket_name)
    print('Bucket created')
    is_bucket_created=True
else:
    print('Bucket name already exists in s3 bucket')

# dealing with Files
file1='file1.txt'
file2='file2.txt'
s3.Bucket('my-bucket').upload_file(
    FileName='file1.txt',   # local file
   key='file2.txt'    # S3 object key
)

# READ and print the file from the bucket
obj=s3.Object('my-bucket', 'file2.txt')
body=obj.get()['Body'].read()
print(body)


# Update file_1 in bucket with new content from file_2

s3.object('my-bucket', 'file2.txt').put(Body=open(file1,'rb'))


#delete the data
s3.delete_object(Bucket='my-bucket', Key='file2.txt')


#delete Bucket if there are no Files
s3.Bucket(bucket_name).delete() # The bucket will be deleted only if there are no files in the s3 bucket


#delete  data + delete the Bucket
#Step 1: Delete all objects (non-versioned bucket)
bucket = s3.Bucket(bucket_name)
bucket.objects.all().delete()

#Step 2: Delete the bucket
bucket.delete()







