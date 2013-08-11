import os
import boto

from boto.s3.connection import S3Connection
from boto.s3.key import Key

def upload_dir_to_s3(source_dir, bucket):
    conn = boto.connect_s3(os.getenv('AWS_ACCESS_KEY_ID'),
                           os.getenv('AWS_SECRET_ACCESS_KEY'))
    b = conn.get_bucket(bucket)
    k = Key(b)

    for dir_path, dir_names, filenames in os.walk(source_dir):
        for file in filenames:
            file_path = os.path.join(dir_path, file)
            s3_path = os.path.relpath(file_path, source_dir)
            print("sending: %s\n" % s3_path)
            k.key = s3_path
            k.set_contents_from_filename(file_path)
            k.set_acl('public-read')

if __name__ == "__main__":
    upload_dir_to_s3('../publish/127.0.0.1:8000/', 'petexgraham.com')