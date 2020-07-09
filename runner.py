import os 

l = []
for i in range(1,5):
    ch = str(i) + "0000"

    for j in range(0, 101):

        os.system('python generate_conditional_samples_to_file.py --model_name model_{} --length 700 --seed {} --temperature 1.0 --top_k 50 --top_p 1.0 --nsamples 1 --raw_text "The eternal sky "'.format(ch, j))


