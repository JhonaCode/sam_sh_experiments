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
from    Parameters_large  import *
from    Parameters_medium import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc

import  datetime as dt 


#separate with coma

var         =   ['MCUP']        

###############################################
#figures name
#####################
###RESUMEN
#figures name
#####################

exp         =  [ 
               small,
               s_w_m,
               s_t_m_wshf_l,
               medium,
               s_qt_m_wshf_l,
               large,
               ]

ar=r'$\rightarrow$'
ls='$\mathrm{_{ls}}$'

exp_label   =  [
                'Small(S)',
                '+W(M)',
                r'+$\theta$%s(M)+[W,SH](L)'%(ls),
                'Medium (M)' ,  
                r'+[q%s,$\theta$%s](M)+[W,SH](L)'%(ls,ls),
                'Large(L)'
               ]

fig_name='s2m2l_final'



xlabel='uMF [kgm$^{2}$s$^{-1}]$'


color_exp=[
            [[1,0]    ,'blue'],
            [[2,2,1,2],'navy'],
            [[1,0]    ,'purple'],
            [[1,0]    ,'Orange'],
            [[1,1]    ,'green'],
            [[1,0]    ,'red'],
          ]


########################################################
########################################################

lim         =  [
                (0,0.10),
               ]
alt         =  [
                 (0,3.5), 
               ]

var_to      =  [
                    1 
               ]

#text(x,y),loc,z,x,legend
l1           =  ( 0.001,0.15,'upper right',True,True,True)

leg_loc      =  [ 
                  l1
                ]

show       =  [
                True
               ]

diurnal     =  [
                True
              ]

exp_label_2  =  [
                 r'a)Small%sLarge 11H'%ar ,  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,11,fig_name,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)

#text(x,y),loc,z,x,legend
l1           =  ( 0.001,0.15,'upper right',False,True,False)

leg_loc      =  [ 
                  l1
                ]

exp_label_2  =  [
                 r'b)Small%sLarge 14H'%ar ,  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,14,fig_name,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)



l1           =  ( 0.002,0.15,'upper right',False,True,False)

leg_loc      =  [ 
                  l1
                ]

exp_label_2  =  [
                 r'b)Small%sLarge 17H'%ar ,  
                ]

dc.diurnal_exp_var_hour_sam(exp,var,17,fig_name,explabel=exp_label,explabel2=exp_label_2,xlabel=xlabel,alt=alt,leg_loc=leg_loc,lim=lim,color=color_exp,show=show,diurnal=diurnal)

