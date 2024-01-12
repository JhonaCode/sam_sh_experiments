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

#exp1=small
#exp2=medium
#case=' Medium-Small'


exp1=medium
exp2=large
case=' Large-Medium'

##
#exp1=small
#exp2=large
#case=' Large-Small'


#separate with comak 
exp_label   = [
                  #r'a) $\mathrm{\theta_v}$'+case,r'b) RH'+case, r'c) W'+case, 
                  r'd) $\mathrm{\theta_v}$'+case,r'e) RH'+case, r'f) W'+case, 
#                 r'$\mathrm{\theta_v}$'+case,r' RH'+case, r' W'+case, 
#                r'a) $\mathrm{\theta}_{ls}$'+case, r'b) q$_{ls}$'+case, r'c) W'+case, 
] 

var         =  ['THETAV','RELH','WOBS',]

#print(small.QVOBS.units)
#print(small.WOBS.units)
#print(small.THETAV.units)

c1=(-2.0   ,2.0   ,21,'[K]')
c2=(-30    ,30    ,21,'[%]')
c3=(-1.5   ,1.5   ,21,'[cms$^{-1}$]')

#c1=(-5     ,5    ,21,'[Kday$^{-1}$]')
#c2=(-5     ,5    ,21,'[gkg$^{-1}$day$^{-1}$]')
#c3=(-1.5   ,1.5    ,21,'[cms$^{-1}$]')

contour     =[
              c1,c2,c3
             ]


var_to      =  [
                  1,1,100
               ]

alt         =  [
                3.5, 3.5, 3.5, 3.5, 3.5,
               ]

co1='RdBu_r'

color       =  [
                co1,co1,co1,co1,co1
               ]

####bar x,y axis, top_lfc_pbl,cm a mais do grafico
a1          =  (True,True,True ,True,0.35,1.34)
a2          =  (True,True,False,True,0.35,1.28)
a3          =  (True,True,False,True,0.35,1.28)
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


