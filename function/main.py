import json

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()


def print_labels(labels):
    print('Labels:')
    for label in labels:
        print(label.description)


def main(request):
    if request.method == "POST":
        file = request.files["file"]
        content = file.read()

        image = vision.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        print_labels(labels)

        return json.dumps(labels), 200

    return "Not Found", 404
