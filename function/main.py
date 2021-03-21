import json

# Imports the Google Cloud client library
from google.cloud import vision

HEADERS = {
    "Access-Control-Allow-Origin": None,
    "Access-Control-Allow-Methods": "POST",
    "Content-Type": "application/json",
}

# Instantiates a client
client = vision.ImageAnnotatorClient()


def main(request):
    HEADERS["Access-Control-Allow-Origin"] = request.headers.get("origin")  # Allow all origin
    if request.method == "POST":
        file = request.files["file"]
        content = file.read()

        image = vision.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        result = [{"label": label.description, "score": label.score} for label in labels]

        return json.dumps(result), 200, HEADERS

    return "Not Found", 404, HEADERS
