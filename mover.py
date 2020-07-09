import os
import shutil

# os.path.abspath("the_file.txt")
# path = os.getcwdb()
# print ("The current working directory is %s" % path)
# path = os.getcwd()
# print ("The current working directory is %s" % path)

base_path = "C:\\Users\\MASTER\\GPT2_REGULAR\\gpt2_regular_clean_02_07\\checkpoint\\run1"

source = "C:\\Users\\MASTER\\GPT2_REGULAR\\gpt2_regular_clean_02_07\\models\\124M\\"

source_1 = source + "encoder.json"
source_2 = source + "hparams.json"
source_3 = source + "vocab.bpe"

target_path = "C:\\Users\\MASTER\\GPT2_REGULAR\\gpt2_regular_clean_02_07\\models"
# os.mkdir(target_path)


l =[]
for z in range(1,34):
    l.append(z * 1000)

for i in l:
    path = target_path + "\\model_{}".format(str(i))

    os.mkdir(path)
  
    for j in os.listdir(base_path):
    
        if ("model-" + str(i) + ".") in j:
            print(j)
            
            fb = base_path + "\\" + j
            ft = path + "\\" + j
            
            shutil.copy(fb, ft)
            print("fb: ", fb)
            print("ft: ", ft)
            
    target_1 = path + "\\" + "encoder.json"
    target_2 = path + "\\" + "hparams.json"
    target_3 = path + "\\" + "vocab.bpe"
    
    shutil.copy(source_1, target_1)
    shutil.copy(source_2, target_2)
    shutil.copy(source_3, target_3)
    
    checkpoint_path = path + "\\" + "checkpoint"
    f = open(checkpoint_path, "w", encoding="utf-8")
    write_str=('model_checkpoint_path: "model-{}"\nall_model_checkpoint_paths: "model-{}"'.format(str(i),str(i)))
    f.write(write_str)
    f.close()
    
    
  ## RUN MODELS:  
# for y in nums:
    # os.system('python generate_conditional_samples_to_file.py --model_name model_{} --length 300 --seed 50 --temperature 1.0 --top_k 50 --top_p 1.0 --nsamples 1 --raw_text "The eternal sky "'.format(str(y)))
            
            
            
            
