CUDA_VISIBLE_DEVICES=0 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True torchrun --standalone --nproc_per_node=1 sample_video.py \
--base configs/tora/model/cogvideox_5b_tora_i2v.yaml configs/tora/inference_sparse.yaml \
--load ckpts/tora/i2v \
--output-dir samples \
--point_path my_trajs/trajectory_coords_deadpool.txt \
--input-file assets/text/i2v/deadpool.txt \
--img_dir assets/images \
--image2video