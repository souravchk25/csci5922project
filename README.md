
# Occupancy Network based 3D Image Reconstruction usingSingle-Depth View

## (1) Architecture
![Arch_Image](https://github.com/Yang7879/3D-RecGAN-extended/blob/master/3D-RecGAN%2B%2B_arch.png)
## (2) Sample Results
![Teaser_Image](https://github.com/Yang7879/3D-RecGAN-extended/blob/master/3D-RecGAN%2B%2B_sample.png)

## (3) Data
#### Part 1: {ShapeNetCore.v2: bench, chair, couch, table}, 20G
[https://drive.google.com/open?id=1rmOggF0ivB42KozMX3sQGD1CkZNOGCmM](https://drive.google.com/open?id=1rmOggF0ivB42KozMX3sQGD1CkZNOGCmM)
#### Part 2: {ShapeNetCore.v2: airplane, car, monitor, faucet, guitar, gun}, 9.3G
[https://drive.google.com/open?id=1zLQd68O73ZiwZ8S8qsLwwGYDcC5PiEdG](https://drive.google.com/open?id=1zLQd68O73ZiwZ8S8qsLwwGYDcC5PiEdG)
#### Real Dataset: {Kinect: bench, chair, couch, table}
[https://drive.google.com/open?id=1wTE721q0r66Z6yyN68O1Tz4Bg5-aYnq3](https://drive.google.com/open?id=1wTE721q0r66Z6yyN68O1Tz4Bg5-aYnq3)


## (4) Requirements
python 2.7.6

tensorflow 1.2.0

numpy 1.13.3

scipy 0.19.0

matplotlib 2.0.2

skimage 0.13.0

## (5) Run
#### Training
```
source venv/bin/activate
python main_3D-RecGAN++.py
```
#### Test Demo (Download model first)
python demo_3D-RecGAN++.py

### Web Application Run Locally
```
source venv/bin/activate
python main.py
```

## (6) Citation
```
@inProceedings{Yang18,
  title={Dense 3D Object Reconstruction from a Single Depth View},
  author = {Bo Yang
  and Stefano Rosa
  and Andrew Markham
  and Niki Trigoni
  and Hongkai Wen},
  booktitle={TPAMI},
  year={2018}
}
```

System Requirements:

Google Cloud Platform - Deep Learning VM
Input Framework: PyTorch 1.4 + fast.ai 1.0 (CUDA 10.0)
GPU: 1, nvidia-tesla-k80

We have referred to the code provided by the following citation for our implementation:
```
@inproceedings{Occupancy Networks,
    title = {Occupancy Networks: Learning 3D Reconstruction in Function Space},
    author = {Mescheder, Lars and Oechsle, Michael and Niemeyer, Michael and Nowozin, Sebastian and Geiger, Andreas},
    booktitle = {Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)},
    year = {2019}
}
```

Our modifications to the original architecture is documented within the code.

# Installing required packages using anaconda3, run the following commands:
conda env create -f environment.yaml
conda activate mesh_funcspace

# Compile the required extension modules:
python setup.py build_ext --inplace

# Download the required pre-processed dataset (will be downloaded to data/ShapeNet folder)
# Run in occupancy_networks_code directory.
bash scripts/download_data.sh

# Training:
python train.py <CONFIG_FILE_DIRECTORY/onet.yaml>

# Generation using pre-trained model:
python generate.py <CONFIG_FILE_DIRECTORY/onet_pretrained.yaml
