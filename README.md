# Contact-GraspNet  

- Adding docker implementation by [Jishnu P](https://jishnujayakumar.github.io/).

## Installation

This code has been tested with python 3.7, tensorflow 2.2, CUDA 11.3, Docker Compose version v2.24.5

- Build the docker image (this only needs to do once and can take some time).
  ```shell
  ./build_docker_image.sh
  ```

- To run the container
  ```shell
  ./start_docker.sh # in detached mode (default)
  ./start_docker.sh -i # in interactive mode
  ```

- To stop:
  ```shell
  ./stop_docker.sh
  ```

- To enter the container:
  ```shell
  ./enter_docker.sh
  ```


Create the conda env
```
conda env create -f jp_cgnet.yml
```

Download data and ckpts
```python
python download_artifacts.py
```

### Troubleshooting

- Recompile pointnet2 tf_ops:
```shell
sh compile_pointnet_tfops.sh
```

### Hardware
Inference done and tested on 1x Nvidia A5000 GPU 24GB VRAM


## Inference


Contact-GraspNet can directly predict a 6-DoF grasp distribution from a raw scene point cloud. However, to obtain object-wise grasps, remove background grasps and to achieve denser proposals it is highly recommended to use (unknown) object segmentation [e.g. [1](https://github.com/chrisdxie/uois), [2](https://arxiv.org/abs/2103.06796)] as preprocessing and then use the resulting segmentation map to crop local regions and filter grasp contacts.

Given a .npy/.npz file with a depth map (in meters), camera matrix K and (optionally) a 2D segmentation map, execute:

```shell
python contact_graspnet/inference.py \
       --np_path=test_data/*.npy \
       --local_regions --filter_grasps
```

<p align="center">
  <img src="examples/7.png" width="640" title="UOIS + Contact-GraspNet"/>
</p>
--> close the window to go to next scene

Given a .npy/.npz file with just a 3D point cloud (in meters), execute [for example](examples/realsense_crop_sigma_001.png):
```shell
python contact_graspnet/inference.py --np_path=/path/to/your/pc.npy \
                                     --forward_passes=5 \
                                     --z_range=[0.2,1.1]
```

`--np_path`: input .npz/.npy file(s) with 'depth', 'K' and optionally 'segmap', 'rgb' keys. For processing a Nx3 point cloud instead use 'xzy' and optionally 'xyz_color' as keys.  
`--ckpt_dir`: relative path to checkpooint directory. By default `checkpoint/scene_test_2048_bs3_hor_sigma_001` is used. For very clean / noisy depth data consider `scene_2048_bs3_rad2_32` / `scene_test_2048_bs3_hor_sigma_0025` trained with no / strong noise.   
`--local_regions`: Crop 3D local regions around object segments for inference. (only works with segmap)  
`--filter_grasps`: Filter grasp contacts such that they only lie on the surface of object segments. (only works with segmap)  
`--skip_border_objects` Ignore segments touching the depth map boundary.  
`--forward_passes` number of (batched) forward passes. Increase to sample more potential grasp contacts.  
`--z_range` [min, max] z values in meter used to crop the input point cloud, e.g. to avoid grasps in the foreground/background(as above).  
`--arg_configs TEST.second_thres:0.19 TEST.first_thres:0.23` Overwrite config confidence thresholds for successful grasp contacts to get more/less grasp proposals 

## Citation

```
@article{sundermeyer2021contact,
  title={Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes},
  author={Sundermeyer, Martin and Mousavian, Arsalan and Triebel, Rudolph and Fox, Dieter},
  booktitle={2021 IEEE International Conference on Robotics and Automation (ICRA)},
  year={2021}
}
```
