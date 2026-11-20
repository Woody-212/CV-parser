import boto3

textract = boto3.client("textract", region_name="eu-west-1")



def extract_text(bucket, key):
    lines = []
     
    response = textract.detect_document_text(
    Document = {"S3Object": {"Bucket": bucket, "Name": key}}
    )

    for block in response["Blocks"]:
        if block["BlockType"] == "LINE":
            lines.append(block["Text"])

    return "\n".join(lines)

print(extract_text("luke-cv-parser-uploads-2026", "cv.pdf"))