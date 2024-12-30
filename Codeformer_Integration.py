# Codeformer install with requirements

!git clone https://github.com/sczhou/CodeFormer.git
%cd CodeFormer
!pip install -r requirements.txt

!pip install gfpgan basicsr facexlib

import os
import torch
from torchvision import transforms
from PIL import Image

# Upgrade torch and torchvision to the latest versions
!pip install --upgrade torch torchvision

# Navigate to the basicsr directory and install it
%cd /content/CodeFormer/basicsr
!python setup.py develop

# Navigate back to the main CodeFormer directory
%cd /content/CodeFormer

# Download facelib pretrained models
!python scripts/download_pretrained_models.py facelib

# Download dlib pretrained models (optional, only if needed)
!python scripts/download_pretrained_models.py dlib

# Download CodeFormer pretrained models
!python scripts/download_pretrained_models.py CodeFormer



import os
import torch
from torchvision import transforms
from PIL import Image

# Navigate to the top-level CodeFormer directory
%cd /content/CodeFormer

# Install dependencies from the requirements.txt file
!pip install -r requirements.txt
!pip install gfpgan basicsr facexlib

# Download facelib pretrained models
!python scripts/download_pretrained_models.py facelib

# Download dlib pretrained models (optional, only if needed)
!python scripts/download_pretrained_models.py dlib

# Download CodeFormer pretrained models
!python scripts/download_pretrained_models.py CodeFormer


from google.colab import files
import os

# Upload your images to Colab
# This will be the location to integrate *gdown* for accessing 
# Files from the Kingdom files on Google Drive 
uploaded = files.upload()

# Create an input folder for test images if not exists
input_folder = "./inputs/test_images"
os.makedirs(input_folder, exist_ok=True)

# Save uploaded images into the inputs/test_images directory
for filename in uploaded.keys():
    with open(os.path.join(input_folder, filename), "wb") as f:
        f.write(uploaded[filename])


!python inference_codeformer.py --w 1.0 --input_path ./inputs/TestWhole --output_path ./results


# Zip the results directory for easier download
!zip -r results.zip ./results

# Download the results
files.download('results.zip')



# Step 1: Clone CodeFormer repository and navigate to the directory
!git clone https://github.com/sczhou/CodeFormer.git
%cd CodeFormer

# Step 2: Install dependencies from requirements.txt
!pip install -r requirements.txt

# Step 3: Install additional packages like gfpgan, basicsr, and facexlib
!pip install gfpgan basicsr facexlib

# Install basicsr directly from PyPI
!pip install basicsr

# Download facelib pretrained models
!python scripts/download_pretrained_models.py facelib

# Download dlib pretrained models (optional, only if needed)
!python scripts/download_pretrained_models.py dlib

# Download CodeFormer pretrained models
!python scripts/download_pretrained_models.py CodeFormer



# Step 4: Install basicsr package properly from setup.py
%cd /content/CodeFormer/basicsr
!python setup.py develop

# Step 5: Navigate back to the CodeFormer directory
%cd /content/CodeFormer

# Test importing basicsr
import basicsr

# Step 6: Download pretrained models using the provided script
!python scripts/download_pretrained_models.py facelib   # Download facelib models
!python scripts/download_pretrained_models.py dlib      # Download dlib models (optional)
!python scripts/download_pretrained_models.py CodeFormer # Download CodeFormer models

