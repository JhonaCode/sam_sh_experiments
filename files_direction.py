import os

#Repository location 
#computer   = '/home/jhona'
#Figure out folder  
#path = "%s/repositories/sam/SAM6.11.4/GOAMAZON_LES/python/stat/testes_xc50/fig"%(computer)

#Repository location 
computer   = '/home/jhonatan.aguirre'
#Figure out folder  
#path = "%s/sam_sh_experiments/document/fig"%(computer)
path = "%s/sam_sh_experiments/document/fig_final"%(computer)

# Check if the directory exists
if not os.path.exists(path):
    # If it doesn't exist, create it
    os.makedirs(path)


file_fig= path
file_temporal= path

#Size in inches to make the temporal plots
tplot_size=1.0

"""
####################################2d
#Repository location 
computer   = '/home/jhonatan.aguirre'
#Figure out folder  
#path = "%s/sam_sh_experiments/document/fig"%(computer)
path = "%s/sam_sh_experiments/document/fig_2d"%(computer)

# Check if the directory exists
if not os.path.exists(path):
    # If it doesn't exist, create it
    os.makedirs(path)


file_fig= path
file_temporal= path
"""
