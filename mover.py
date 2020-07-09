import os
import shutil

base_path = "/content/GPT2_REGULAR/checkpoint/run1"
source = "/content/GPT2_REGULAR/models/124M/"

source_1 = source + "encoder.json"
source_2 = source + "hparams.json"
source_3 = source + "vocab.bpe"

target_path = "/content/GPT2_REGULAR/models"

l =[]
for z in range(1,5):
    l.append(z * 10000)

for i in l:
    path = target_path + "/model_{}".format(str(i))

    os.mkdir(path)
  
    for j in os.listdir(base_path):
    
        if ("model-" + str(i) + ".") in j:
            print(j)
            
            fb = base_path + "/" + j
            ft = path + "/" + j
            
            shutil.copy(fb, ft)
            print("fb: ", fb)
            print("ft: ", ft)
            
    target_1 = path + "/" + "encoder.json"
    target_2 = path + "/" + "hparams.json"
    target_3 = path + "/" + "vocab.bpe"
    
    shutil.copy(source_1, target_1)
    shutil.copy(source_2, target_2)
    shutil.copy(source_3, target_3)
    
    checkpoint_path = path + "/" + "checkpoint"
    f = open(checkpoint_path, "w", encoding="utf-8")
    write_str=('model_checkpoint_path: "model-{}"\nall_model_checkpoint_paths: "model-{}"'.format(str(i),str(i)))
    f.write(write_str)
    f.close()
           
