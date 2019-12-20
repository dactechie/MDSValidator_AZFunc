import os
from ..logger import logger

def get_latest_data_file(dir='input'):
    import glob
    
    list_of_files = glob.glob(os.path.join(dir,'*.csv')) # * means all if need specific format then *.csv
    if not any(list_of_files):
        logger.error("no input csv file in the input folder !")
        return None

    return max(list_of_files, key=os.path.getctime)



def get_result_filename(full_input_fname, all_eps=True, program='TSS'):
    if not all_eps:
        output_fname_tags =f'{program}_closed_eps_period'
    else:
        output_fname_tags = f'{program}_with_open_eps_period'
    
    base_dir = os.sep.join(full_input_fname.split(os.sep)[:-2])
    output_dir =  os.path.join(base_dir, "output")
    
    inp_name, inp_ext = os.path.splitext(os.path.basename(full_input_fname)) 
    return os.path.join(output_dir, f"{inp_name}_{output_fname_tags}{inp_ext}")