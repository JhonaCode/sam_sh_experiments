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
from    Parameters         import small
from    Parameters_medium  import medium
from    Parameters_large   import large

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.two_dimensional   as two


exp1=small
exp2=large
case=' Large-Small'

exp1=small
exp1=medium
exp2=large
case=' Large-Medium'

exp1=small
exp1=small
exp2=medium
case=' Medium-Small'


#separate with comak 
#exp_label   =  ['a) $\theta_v_{obs}$'+case, 'b) w$_{obs}$'+case, 'c) q$_v_{obs}$'+case,
exp_label   =  [
                r'a) $\mathrm{\theta}_v$'+case, r'b) w'+case, r'c) q$_v$'+case, 
                ] 

var         =  ['THETAV','WOBS','QVOBS']

#print(small.QVOBS.units)
#print(small.WOBS.units)
#print(small.THETAV.units)

c1=(-2.0   ,2.0    ,21,'[K]')
c2=(-1.5   ,1.5    ,21,'[cms$^{-1}$]' )
c3=(-1.5   ,1.5    ,21,'[gkg$^{-1}$]')

contour     =[
              c1,c2,c3,
             ]


var_to      =  [
                  1,100,1,
               ]

alt         =  [
                3.5, 3.5, 3.5,
               ]

co1='RdBu_r'

color       =  [
                co1,co1,co1,
               ]

####bar ,y axis, top_lfc_pbl,cm a mais do grafico
a1          =  (True,True ,False,0.35,1.34)
a2          =  (True,False,False,0.35,1.28)
a3          =  (True,False,False,0.35,1.28)
axis_on     =  [a1,a2,a3,]


show       =  [
                 True,True,True,
                 #False,False,False,False
              ]

days        = [ 
                [(2014,1,1,8),(2014,1,1,20)],
                [(2014,1,1,8),(2014,1,1,20)],
                [(2014,1,1,8),(2014,1,1,20)],
                [(2014,1,1,8),(2014,1,1,20)],
            ]


two.plot2d_im_diff(exp1,exp2,var,alt=alt,days=days,color=color,explabel=exp_label,var_to=var_to,contour=contour,axis_on=axis_on,show=show)


