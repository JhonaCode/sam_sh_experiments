################################################################
#Program to plot meteorological date
#of the OUT_STAT files of SAM with
#python and  Netcdf library.

###########################
#Modified:23/01/23
# To run using the same files
# python_src files

###########################
#Create by: Jhonatan Aguirre
#Date:07/04/2022
#working
#python 3.9

################################################################
# To activate this environment, use
#
# $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
# $ conda deactivate
#
# path of the ncfile or data to plot
from    Parameters import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc

import  datetime as dt 


#separate with colon

exp         =  [ 
               small,
               s_shf_l,
               #s_lhf_l,
               #s_hf_l,
               #s_q_l,
               #s_wshf_l,
               #s_wlhf_l,
               #s_wqthf_l,
               #s_wshft_l,
               #s_shft_l,
               #s_wqthfuv_l,
               #s_t_l,
               #s_tinit_l,
               #large
               #shca_q_l 
               #m_q_l 
               #m_wq_l 
               #m_wqhf_l 
               #m_halflhf 
               #l_shf_s
                ]

var         =   ['MCUP','QC']        
#figures name
exp_label   =  [ 
                ['S Mf', 'S ql'],
                ['S Mf', 'S ql'],
               ]

lim         =  [
                [(0,0.1),(0,0.7)],
                [(0,0.1),(0,0.1)]
               ]

var_to      =  [
                    [1 ,1],  
                    [1 ,1],  
               ]


l1           =  ( 0.001,2.8,'upper right',True,True)
l2           =  ( 0.001,2.8,'upper right',True,True)
l3           =  ( 0.001,2.8,'upper right',True,True)

leg_loc      =  [ 
                  [l1,l2],
                  [l1,l2],
                ]

alt         =  [
                 [3.0, 3.0], 
                 [3.0, 3.0], 
               ]

color       =  [
                ['black','black'],
                ['black','black'],
               ]

show       =  [
                [True,True],
                [True,True],
               ]

diurnal     =  [
                [True,True],
                [True,True],
              ]


dc.diurnal_hours_exp_var_sam(exp,var,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)

