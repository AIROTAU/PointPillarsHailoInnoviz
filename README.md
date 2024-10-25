# Real-Time 3D Object Detection Using InnovizOne LiDAR and Low-Power Hailo-8 AI Accelerator

## Abstract

[Object detection is a significant field in autonomous driving. Popular sensors for this task include cameras and LiDAR sensors. LiDAR sensors offer several advantages, such as insensitivity to light changes and the ability to provide 3D information in the form of point clouds, which include the ranges of objects. However, 3D detection methods, such as PointPillars, typically require high-power hardware. Additionally, most common spinning LiDARs are sparse and may not achieve the desired quality of object detection in front of the car. In this paper, we present the feasibility of performing real-time 3D object detection of cars using 3D point clouds from a LiDAR sensor, processed and deployed on a low-power Hailo-8 AI accelerator. The LiDAR sensor used in this study is the InnovizOne sensor, which captures objects in higher quality compared to spinning LiDAR techniques, especially for distant objects. We successfully achieved real-time inference at a rate of approximately 5Hz with a high accuracy of 0.79% F1 score, with only -0.2% degradation compared to running the same model on an NVIDIA GeForce RTX 2080 Ti. This work demonstrates that effective real-time 3D object detection can be achieved on low-cost, low-power hardware, representing a significant step towards more accessible autonomous driving technologies.  The source code and the pre-trained models are available at]

## Introduction
[This project demonstrates the capability of achieving accurate 3D object detection using low-power chips. We utilized a dataset created from our own recordings with an - - InnovizOne LiDAR to train the PointPillars model via the OpenPCDet framework. Real-time inference was then performed using our low-power Hailo-8 AI accelerator.

In this repository, you will find our modified configuration for the model and a script for real-time inference using Innoviz data. This is based on Hailo's script available in their application code examples: [Hailo Application Code Examples](https://github.com/hailo-ai/Hailo-Application-Code-Examples/tree/main)
.]

## Usage
1. **Train the Model on a Custom Dataset**
    - Follow the guidance provided in [Hailo Application Code Examples](https://github.com/hailo-ai/Hailo-Application-Code-Examples/tree/main) to train the model using your dataset.
2. **Perform Real-Time Inference**
    - After training your model, follow the instructions in the InferenceOnly_Hailo_Innoviz_PointPillars_POC.ipynb file to achieve real-time inference.

> **Note:** The configuration file for the PointPillars model provided in this repository (''point_pillar_best.yaml'') has been adjusted to best suit our dataset and may not necessarily produce optimal results with your own dataset.