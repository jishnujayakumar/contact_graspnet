
# ✋ **Contact-GraspNet**

📦 **Docker support added by [Jishnu P](https://jishnujayakumar.github.io/)**  

https://github.com/user-attachments/assets/ac772b72-594b-4938-b4aa-34e06d852207

---

## 🚀 **Installation**

✅ This code has been tested with:
- Python 3.7  
- TensorFlow 2.5  
- CUDA 11.3  
- Docker Compose v2.24.5  

---

### 🛠 **Docker Setup**

🔨 **Build the Docker image** (only needed once):
```bash
./build_docker_image.sh
```

▶️ **Run the container**:
```bash
./start_docker.sh        # Default: detached mode
./start_docker.sh -i     # Interactive mode
```

🛑 **Stop the container**:
```bash
./stop_docker.sh
```

💻 **Enter the container**:
```bash
./enter_docker.sh
```

---

### 🐍 **Conda Environment**
```bash
conda env create -f jp_cgnet.yml
```

---

### 📥 **Download Data and Checkpoints**
```bash
python download_artifacts.py
```

---

### 🛠 **Troubleshooting**

🔄 **Recompile PointNet2 TensorFlow Ops**:
```bash
sh compile_pointnet_tfops.sh
```

---

### ⚙️ **Hardware**
Tested on:  
- **1x NVIDIA A5000 GPU (24GB VRAM)**

---

## 🧠 **Inference**

Contact-GraspNet can **predict 6-DoF grasp distributions from raw point clouds**.  
For best results:
- Use an **object segmentation method** (e.g., [UOIS](https://github.com/chrisdxie/uois), [YCB-V](https://arxiv.org/abs/2103.06796)) to segment objects.  
- Crop and filter grasp contacts based on segments.  

🔍 **Run with Depth Map (.npy/.npz)**:
```bash
python contact_graspnet/inference.py \
--np_path=test_data/*.npy \
--local_regions \
--filter_grasps
```



<p align="center">
  <img src="examples/7.png" width="640" title="UOIS + Contact-GraspNet"/>
</p>
(Click window to advance to next scene)

🔍 **Run with Point Cloud (.npy/.npz)**:
```bash
python contact_graspnet/inference.py \
--np_path=/path/to/your/pc.npy \
--forward_passes=5 \
--z_range=[0.2,1.1]
```

---

### 📝 **Key Options**
- `--np_path`: Input .npz/.npy with keys 'depth', 'K', optionally 'segmap', 'rgb'. For Nx3 point cloud use 'xyz', optionally 'xyz_color'.  
- `--ckpt_dir`: Checkpoint directory (default: `checkpoint/scene_test_2048_bs3_hor_sigma_001`).  
- `--local_regions`: Crop regions around object segments (requires `segmap`).  
- `--filter_grasps`: Filter contacts to segment surfaces (requires `segmap`).  
- `--skip_border_objects`: Ignore segments on map boundary.  
- `--forward_passes`: Increase for more grasps.  
- `--z_range`: [min, max] depth cropping (in meters).  
- `--arg_configs`: Override thresholds (e.g., `TEST.second_thres:0.19 TEST.first_thres:0.23`).  

---

## 📚 **Citation**

```bibtex
@article{sundermeyer2021contact,
  title={Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes},
  author={Sundermeyer, Martin and Mousavian, Arsalan and Triebel, Rudolph and Fox, Dieter},
  booktitle={2021 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2021}
}
```

---
