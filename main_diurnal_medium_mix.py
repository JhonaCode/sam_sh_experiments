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
from    Parameters_medium import *

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
                medium, 
                m_q_l, 
                m_t_l, 
                m_shf_l, 
                m_w_l, 
                m_wq_l, 
                m_wshf_l,
                m_shft_l,
                m_wqhf_l, 
                m_wshft_l,
                m_halflhf 
                ]

var         =   ['MCUP']        
#figures name
exp_label   =  [ 
                'M Mf', 
                'M q L Mf', 
                'M T L Mf', 
                'M shf L Mf', 
                'M w L Mf', 
                'M w q L Mf', 
                'M w shf L Mf',
                'M shf T L Mf',
                'M w q hf L Mf', 
                'M w shf T L Mf',
                'M lhf/2 Mf' 
               ]

lim         =  [
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
               ]

var_to      =  [
                    1, 1, 1,  
                    1, 1, 1,  
                    1, 1, 1,  
                    1, 1, 1,  
                    1, 1, 1,  
               ]


l1           =  ( 0.001,2.8,'upper right',True,True)
l2           =  ( 0.001,2.8,'upper right',True,True)
l3           =  ( 0.001,2.8,'upper right',True,True)

leg_loc      =  [ 
                l1,l1,l1,
                l1,l1,l1,
                l1,l1,l1,
                l1,l1,l1,
                l1,l1,l1,
                l1,l1,l1,
                ]

alt         =  [
                3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 
               ]

color       =  [
                'black','black','black',
                'black','black','black',
                'black','black','black',
                'black','black','black',
               ]

show       =  [
                False,False,False,
                False,False,False,
                False,False,False,
                False,False,False,
                False,False,False,
               ]

diurnal     =  [
                True,True,True,
                True,True,True,
                True,True,True,
                True,True,True,
                True,True,True,
              ]

k=0
for ex in exp:

    j=0
    for v in var:

        dc.diurnal_hours_sam(ex,v,explabel=exp_label[k],alt=alt[k],leg_loc=leg_loc[k],lim=lim[k],color=color[k],show=show[k],diurnal=diurnal[k])

        j+=1

    k+=1
