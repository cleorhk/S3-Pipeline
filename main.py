import os
import boto3

def upload_file_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True

if __name__ == "__main__":
    # Define the CSV file and S3 bucket
    file_name = 'src/sapa.csv'
    bucket_name = os.getenv('S3_BUCKET_NAME')
    
    # Upload the file
    success = upload_file_to_s3(file_name, bucket_name)
    if success:
        print(f"File {file_name} uploaded successfully to {bucket_name}.")
    else:
        print(f"File {file_name} failed to upload.")
