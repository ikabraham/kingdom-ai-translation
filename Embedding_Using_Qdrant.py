!pip install qdrant-client
!pip install fastembed

from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct, VectorParams, Distance, Payload
from qdrant_client.http import models as rest
from fastembed import ImageEmbedding
from google.colab import files
import os
from google.colab import userdata
from google.colab import drive
drive.mount('/content/drive')
#could mount with gdown
import os
from pandas import DataFrame
from PIL import Image
from IPython.display import Image, display
from io import BytesIO
import base64
import math

#declare the model for embedding the data
model = ImageEmbedding(model_name="Qdrant/clip-VIT-B-32-vision")

#add the directory of the extracted characters to a variable
base_directory="/content/drive/MyDrive/Servants_of_The_Most_High/Kingdom_with_A.I._Project/WorkBooks/outputChars/char"

#grab each character in the directory
all_image_urls = os.listdir(base_directory)

#log the first ten to check
all_image_urls[:10]

#map the full directory path for each image
sample_image_urls = [os.path.join(base_directory, filename) for filename in all_image_urls]

#check for that the paths are present
sample_image_urls[:10]

#create a dataframe for the characters to store the metadata of the image
payloads = DataFrame.from_records([{"image_url": path} for path in sample_image_urls])
payloads["type"]="character"

payloads.head()

#Iterate over images in dataframe create a pil image from each character
images = [Image.open(path) for path in payloads["image_url"]]

#Check the first character
images[0]

#Check the entire array
images

#resize the images of the pil image references
target_width= 256

def resize_image(image_url):
  pil_image = Image.open(image_url)
  image_aspect_ratio = pil_image.width / pil_image.height
  resized_pil_image = pil_image.resize(
      [target_width, math.floor(target_width * image_aspect_ratio)]
  )
  return resized_pil_image

#function to convert images to base64
def convert_image_to_base64(pil_image):
  image_data = BytesIO()
  pil_image.save(image_data, format="PNG")
  base64_string = base64.b64encode(image_data.getvalue()).decode("utf-8")
  return base64_string

resized_images = list(map(lambda el: resize_image(el), sample_image_urls))
base64_string = list(map(lambda el: convert_image_to_base64(el), resized_images))
payloads["base64"] = base64_string

#print out the payloads that are upsert
payloads

embeddings = list(model.embed(images))
input = embeddings #add embeddings to variable named input

#check out the embeddings
Embeddings

embedding_length = len(embeddings[0])

#confirm the length of the embedding which sets up the database
embedding_length

#set the API Keys
qdrant_api_key = userdata.get('QDRANT_API_KEY')

#access qdrant  to check the collections
qdrant_client = QdrantClient(
    url="https://e63b1e0f-d1fb-48cc-ba71-e5acf0281ee8.europe-west3-0.gcp.cloud.qdrant.io:6333",
    api_key=qdrant_api_key,
)

print(qdrant_client.get_collections())

#declare collections name for the payload objects
collection_name = "test_collection_02"
qdrant_client.delete_collection(collection_name=collection_name)
collection = qdrant_client.create_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(
        size=embedding_length,
        distance=models.Distance.COSINE
        )
)
collection

#formats the payload to a dictionary format to ensure data comes out as a list of records that can be uploaded as metadata
payload_dicts = payloads.to_dict(
    orient="records"
    )
payload_dicts[:2]

#set the records value for the JSON configuration
records = [
    models.Record(
        id=idx,
        payload=payload_dicts[idx],
        vector=embeddings[idx]
    )
for idx, _ in enumerate(payload_dicts)]

#upsert the record payload and its embeddings to qdrant as points
qdrant_client.upload_points(
    collection_name=collection_name,
    points=records
)

# Upload your images to the proper directory
uploaded = files.upload()

# Create an input folder for test images if not exists
input_folder = "./inputs/test_images"
os.makedirs(input_folder, exist_ok=True)

# Loop through each image to upload images into the input_folder
for filename in uploaded.keys():
    with open(os.path.join(input_folder, filename), "wb") as f:
        f.write(uploaded[filename])

#set the directory path to a variable
file_list = os.listdir(input_folder)

#review what’s in the directory
print(file_list)

#loop through the files & create timestamps for selection based on most recent uploads
file_timestamps = {}
for file_name in os.listdir(input_folder):
  file_path = os.path.join(input_folder, file_name)
  file_timestamps[file_name] = os.path.getmtime(file_path)

#check that timestamps exist
file_timestamps

#set variables for the the most recent upload and the most file path
most_recent_file = max(file_timestamps, key=file_timestamps.get)
most_recent_file_path = os.path.join(input_folder, most_recent_file)

#confirm the most recent file was chosen
most_recent_file

#add the most recent file path to a variable
selected_file = most_recent_file_path

# or, to open the image directly:
from PIL import Image
selected_image = Image.open(most_recent_file_path)

#check the image
selected_image

#Need to embed the image and convert the output to show the top ranked images
retrieval_embedding = model.embed(selected_image)

retrieval_embedding = next(retrieval_embedding) # convert the generator object to a numpy array

# Ensure the embedding is a simple list of numbers
new_embedding_data = retrieval_embedding.tolist()  # If retrieval_embedding is a numpy array

#Check that the data is correct
new_embedding_data

#search based on the points

search_result = qdrant_client.query_points(
    collection_name=collection_name,
    query=new_embedding_data,
    #query_text="Which integration is best for agents?"
    limit=10 #adjust to one if you only need the closest result or add more to see more results
    
).points
print(search_result)

#print the image to the workbook
image_data = search_result[0].payload["base64"]
display(Image(data=base64.b64decode(image_data)))

#grab the point of the searched image
search_result[0].id