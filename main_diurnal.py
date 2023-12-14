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
               #large
               #small,
               s_qt_m_w_l,
               s_qt_m_wshf_l,
               s_qt_m_shf_l,
               s_t_m_shf_l,
               s_t_m,
               l_t_m,
               s_qt_m,
               l_shft_m,
               #s_shf_l,
               #s_lhf_l,
               #s_qt_l,
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
               m_wshft_l,
               m_wshf_l,
               #m_q_l 
               #m_wq_l 
               #m_wqhf_l 
               #m_halflhf 
               #shca_q_l 
               shca_shf_l,
               shca_w_l,
               #l_shf_s
                ]

var         =   ['MCUP']        
#figures name
exp_label   =  [ 
                'S q T M w L',
                'M w shf T L',
                'ShCa shf L',
                'ShCa w L',
                'M w shf L',
                'S q T M w shf L',
                'S q T M shf L',
                'S T M shf L',
                'S T M',
                'L T M',
                'S q T M',
                'L shf T  M',
                #'S q T L' ,
                #'S', 'S shf L'  , 'w_ls'],
                #'S hf L MCUP', 'S hf L ql' 
                #'S wq L MCUP', 'S wq L ql'  
                #'S w q t hf L MCUP', 'S w q t hf L ql'  
                #'S w t shf L MCUP', 'S w t shf L ql'  
                #'S  shf t L MCUP', 'S  shf t L ql'  
                #'S  w q hf t uv L MCUP', 'S  w q hf t uv L ql'  
                #'S t L MCUP', 'S t L ql'  
                #'S tinit L MCUP', 'S tinit L ql'  
                #'L MCUP', 'L ql'  
                #' ShCa q L MCUP', 'ShCa q L ql'  
                #' M q L MCUP', 'M q L ql'  
                # 'M wq hf L MCUP', 'M wq hf L ql'  
                # 'M MCUP', 'M ql'  
                # 'M lhf/2' , 'M lhf/2 ql'  
                # 'L shf S' , 'L shf S ql'  
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
