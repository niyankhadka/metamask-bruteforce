import random
import datetime
import os



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
        with open('G:/metamask-bruteforce/wordlists/Raw/bip-0039-english.txt','r') as f: 
            f=f.read()
        f=f.split('\n')
        return f
    except:
        return []
    
def check_and_dump(mapped_keys,get_total_keys):
    dump=1
    if get_total_keys!=[]:
        for i in get_total_keys:
            if i!=mapped_keys:
                pass
            else: 
                dump=0
                break
    
    if dump==1:
        with open('dump_1.txt','a') as f:
            f.write(mapped_keys)
            f.write('\n')
    

def _get_future_time():
    time=input("Enter time to run till using (:) as seperator: ")
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
    
def main_get_all_words():
    #This part of code falls under preprocessing so avoided using it on the loop 

    path_name=input("Enter name of the file mention path if not in same directory: ") 
    #To quit feature added
    if path_name=='q':
        exit()
    #To check for repeatation and remove then in dump_1.txt
    elif path_name=='r':
        recheck_and_dump('dump_1.txt')
        return 0

    word_list=get_all_words_from_file(path_name)
    runtill_variable=_get_future_time()
    #===================================================================================    
    
    #main Process part falls under loops
    while True: 
        print('Let the script run till the end time or you can quit it and resume later\n')
        # current_time=(datetime.datetime.now()).time()
        # current_time = current_time.replace(microsecond=0) 
        get_total_keys=get_all_keys_from_file('dump_1.txt')
        generated_index=generate_unique_index(word_list)
        mapped_keys=map_keys_with_index(word_list,generated_index)
        check_and_dump(mapped_keys,get_total_keys)
        # print('Current Time  || End Time')
        # print(str(current_time)+"      ||  "+str(runtill_variable))
        os.system('cls')
        
        # if current_time>=runtill_variable:
        #     break
    
    #---------------------------------------------------------------------------------


while True: 
    os.system('cls')
    print(' Provide name of the file and time till \n when we want to run this script rest will be dumped on the file dump_1.txt\n \n type r to check dump_1.txt for repetation and avoid them \n type q and enter to quit\n')
    main_get_all_words()