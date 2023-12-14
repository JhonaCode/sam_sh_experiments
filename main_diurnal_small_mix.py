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
var         =   ['MCUP']        

"""
exp         =  [ 
               small,     #1 
               #Uma variavel
               s_shf_l,   #2
               s_lhf_l,   #3
               s_q_l,     #4
               s_t_l,     #5
               s_tinit_l, #6
               s_w_l,     #7
               s_t_m,      #8
               #Duas variaveis
               s_qt_l,    #9
               s_hf_l,    #10
               s_wq_l,    #11
               s_wshf_l,  #12
               s_wlhf_l,  #13
               s_shft_l,  #14
               s_qt_m,     #15
               #Tres variaveis
               s_whf_l,   #16
               s_wshft_l, #17
               s_wqshf_l, #18
               #quatro variaveis
               s_wqthf_l, #19
               s_wqthfuv_l,#20
               #Tres experimentos
"""
"""
exp         =  [
               s_t_m_shf_l,#21
               s_t_m_q_l,#21
               s_t_m_w_l, #22
               s_qt_m_w_l,#23
               s_qt_m_shf_l,#23
               s_qt_m_wshf_l,#24
                ]


#figures name
"""
"""
exp_label   =  [ 
               'S MF',         #1 
               #Uma variavel
               'S shf L MF',   #2
               'S lhf L MF',   #3
               'S q L MF',     #4
               'S T L MF',     #5
               'S Tinit L MF', #6
               'S w L MF',     #7
               'S T M MF',      #8
               #Duas variaveis
               'S q T L MF',    #9
               'S hf L MF',    #10
               'S wq L MF',    #11
               'S w shf L MF',  #12
               'S w lhf L MF',  #13
               'S shf T L MF',  #14
               'S q T M MF',     #15
               #Tres variaveis
               'S w hf L MF',   #16
               'S w shf T L MF', #17
               'S w q shf L MF', #18
               #quatro variaveis
               'S w q T hf L MF', #19
               'S w q T hf uv L MF',#20
               #Tres experimentos
"""
"""
exp_label   =  [ 
               'S T M shf L MF',#21
               'S T M q L MF',#22
               'S T M w L MF',#23
               'S q T M w L MF', #24
               'S q T M shf L MF',#25
               'S q T M w shf L MF',#26
               ]
"""
exp         =  [ 
               s_t_m,      #8
               s_shf_m,      #8
               s_tinit_m,      #8
               s_qt_m,     #15
                ]

exp_label   =  [ 
               'S T M Mf',#21
               'S shf M Mf',#22
               'S Tinit M Mf',#23
               'S q T M Mf',#26
               ]

lim         =  [
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
                (0,0.1),(0,0.1),(0,0.1),
               ]

var_to      =  [
                    1, 1, 1, 1, 1, 1,  
                    1, 1, 1, 1, 1, 1,  
                    1, 1, 1, 1, 1, 1,  
                    1, 1, 1, 1, 1, 1,  
                    1, 1, 1, 1, 1, 1,  
               ]


l1           =  ( 0.001,2.8,'upper right',True,True)
l2           =  ( 0.001,2.8,'upper right',True,True)
l3           =  ( 0.001,2.8,'upper right',True,True)

leg_loc      =  [ 
                l1,l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,l1,
                l1,l1,l1,l1,l1,l1,
                ]

alt         =  [
                3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 
                3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 
                ]

color       =  [
                'black','black','black','black','black','black',
                'black','black','black','black','black','black',
                'black','black','black','black','black','black',
                'black','black','black','black','black','black',
                'black','black','black','black','black','black',
                'black','black','black','black','black','black',
               ]

show       =  [
                False,False,False,False,False,False,
                False,False,False,False,False,False,
                False,False,False,False,False,False,
                False,False,False,False,False,False,
                False,False,False,False,False,False,
                False,False,False,False,False,False,
                False,False,False,False,False,False,
               ]

diurnal     =  [
                True,True,True,True,True,True,
                True,True,True,True,True,True,
                True,True,True,True,True,True,
                True,True,True,True,True,True,
                True,True,True,True,True,True,
                True,True,True,True,True,True,
                True,True,True,True,True,True,
              ]

k=0
for ex in exp:

    j=0

    for v in var:

        dc.diurnal_hours_sam(ex,v,explabel=exp_label[k],alt=alt[k],leg_loc=leg_loc[k],lim=lim[k],color=color[k],show=show[k],diurnal=diurnal[k])

        j+=1

    k+=1
