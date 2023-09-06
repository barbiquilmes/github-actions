import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    """Upload files to S3 bucket."""
    bucket = os.environ["INPUT_BUCKET"]
    bucket_region = os.environ["INPUT_BUCKET_REGION"]
    data_folder = os.environ["INPUT_DATA_FOLDER"]
    tag = os.environ["INPUT_TAG"]

    tag_version = tag.split("/")[-1]

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.client("s3", config=configuration)

    filepaths = []
    for root, subdirs, files in os.walk(data_folder):
        for file in files:
            filename = os.path.join(root, file).replace(data_folder + "/", "")
            filepath = os.path.join(tag_version, filename)
            s3_client.upload_file(
                os.path.join(root, file),
                bucket,
                filepath,
                ExtraArgs={"ContentType": mimetypes.guess_type(file)[0]},
            )
            filepaths.append(filepath)

    # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f's3-filepaths={str(filepaths)}', file=gh_output)

    # website_url = f'http://{bucket}.s3-website-{bucket_region}.amazonaws.com'
    # # The below code sets the 'website-url' output (the old ::set-output syntax isn't supported anymore - that's the only thing that changed though)
    # with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
    #     print(f'website-url={website_url}', file=gh_output)
    #


if __name__ == "__main__":
    run()
