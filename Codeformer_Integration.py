#Mount Gdrive to Colab
from google.colab import drive
drive.mount('/content/drive')

!git clone https://github.com/sczhou/CodeFormer.git
%cd CodeFormer
!pip install -r requirements.txt

!pip install gfpgan basicsr facexlib

!mkdir -p weights
# Download the pretrained models
!wget -P weights https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth
!wget -P weights https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/facelib.pth

import os
import torch
from torchvision import transforms
from PIL import Image

# Upgrade torch and torchvision to the latest versions
!pip install --upgrade torch torchvision

#access the data directory within basicsr
%cd /usr/local/lib/python3.10/dist-packages/basicsr/data

#ensure degradation file is created
!sed -i 's/from torchvision.transforms.functional_tensor/from torchvision.transforms.functional/' degradations.py

#Access the CodeFormer Directory
%cd /content/CodeFormer

# Download facelib pretrained models
!python scripts/download_pretrained_models.py facelib

# Download dlib pretrained models (optional, only if needed)
!python scripts/download_pretrained_models.py dlib

# Download CodeFormer pretrained models
!python scripts/download_pretrained_models.py CodeFormer

#access basicsr directory
%cd /content/CodeFormer/basicsr



#create a versions file
with open('version.py', 'w') as f:
    f.write("__version__ = '1.0.0'\n")
    f.write("__gitsha__ = 'unknown'\n")

#access the codeformer directory
%cd /content/CodeFormer

from google.colab import files

# Upload test images to Colab
uploaded = files.upload()

# Create an input folder for test images if it doesn't already exist
input_folder = "./inputs/TestWhole"
os.makedirs(input_folder, exist_ok=True)

# Save the uploaded images into the input directory
for filename in uploaded.keys():
    with open(os.path.join(input_folder, filename), "wb") as f:
        f.write(uploaded[filename])

# Upload your images to Colab from Google Drive instead of the upload
# This will be the location to integrate *gdown* for accessing 
# Files from the Kingdom files on Google Drive 
uploaded = files.upload()

#run the inference on the file in your folder
# Run the inference script with the correct argument
!python inference_codeformer.py --fidelity_weight 1.0 --input_path ./inputs/test_images --output_path ./results

# Zip the results directory for easier download
!zip -r results.zip ./results

# Download the results
files.download('results.zip')