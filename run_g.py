import os

nums = [1000, 2000, 3000, 4000] 

for i in nums: 
    os.system('python run_generation.py --model_type gpt2 --temperature 1.0 --top_k 50 --top_p 1.0 --model_name_or_path output/checkpoint-{} --length 300 --prompt "Immense light" --seed 68 --num_samples 1'.format(str(i))) 
