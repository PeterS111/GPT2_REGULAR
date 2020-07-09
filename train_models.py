import os 

os.system('python train.py --dataset input_data/Shelley_4a_train.txt --model_name 124M --top_k 50 --top_p 1.0 --save_every 100 --sample_every 100000 --max_to_keep 1000 --val_dataset input_data/Shelley_4a_val.txt --val_every 50 --val_batch_count 40')
