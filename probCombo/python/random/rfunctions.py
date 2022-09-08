# -------------------------------------
# Program Starts from here
# ------------------------------------- 

import random
import datetime
import os
import time

def get_all_words_from_file(path):
    with open(path,'r') as f: 
        f=f.read()
    f=f.split('\n')
    return f


def generate_unique_index(word_list):
    indices=[]
    while True: 
        indices.append(random.randrange(0,len(word_list)))
        indices=list(set(indices))
        if len(indices)==12:
            break
    return indices


def map_keys_with_index(word_list,generated_index):
    final_list=[]
    for i in generated_index:
        final_list.append(word_list[int(i)])
    final_list=' '.join(final_list)
    return final_list


def get_all_keys_from_file(path):
    try: 
        with open(path,'r') as f: 
            f=f.read()
        f=f.split('\n')
        return f
    except:
        return []
    

def check_and_dump(mapped_keys,get_total_keys, dump_file_name):
    dump=1
    if get_total_keys!=[]:
        for i in get_total_keys:
            if i!=mapped_keys:
                pass
            else: 
                dump=0
                break
    
    if dump==1:
        with open(dump_file_name,'a') as f:
            f.write(mapped_keys)
            f.write('\n')


def _get_future_time(end_time):
    time=end_time
    time=time.split(':')
    time=[int(i) for i in time]
    time=datetime.time(time[0],time[1],time[2])
    return time


def recheck_and_dump(path):
    try: 
        with open(path,'r') as f:
            f=f.read()
        f=f.split('\n')
        f=list(set(f))
        total_keys='\n'.join(f)
        with open(path,'w') as f:
            f.write(total_keys)
    except:
        print('Not found text')


def main_get_all_words(worldlist_path, dump_file_name, move_file_name, end_time):
    #This part of code falls under preprocessing so avoided using it on the loop 

    path_name= worldlist_path
    #To quit feature added
    if path_name=='q':
        exit()
    #To check for repeatation and remove then in dump_file_name
    elif path_name=='r':
        recheck_and_dump(dump_file_name)
        return 0

    word_list=get_all_words_from_file(path_name)
    runtill_variable=_get_future_time(end_time)
    #===================================================================================    
    
    #main Process part falls under loops
    while True: 
        print('Random generating script is running....\n')
        current_time=(datetime.datetime.now()).time()
        current_time = current_time.replace(microsecond=0)
        get_total_keys=get_all_keys_from_file(dump_file_name)
        generated_index=generate_unique_index(word_list)
        mapped_keys=map_keys_with_index(word_list,generated_index)
        check_and_dump(mapped_keys,get_total_keys, dump_file_name)
        print('Current Time  || End Time')
        print(str(current_time)+"      ||  "+str(runtill_variable))
        os.system('cls')
        
        if current_time>=runtill_variable:
            os.rename(dump_file_name, move_file_name)
            time.sleep(90)
    
    #---------------------------------------------------------------------------------
