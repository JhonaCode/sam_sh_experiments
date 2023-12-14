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
#exp1=medium
exp2=large

case=' L-S'
#separate with comak 
exp_label   =  ['diff RHS'+case,'diff q$_v$ '+case, 'diff W '+case, 
                'diff U obs'+case, 'diff V obs'+case,'diff THETAV'+case,
                'diff TABS'+case
                ] 

var         =  ['RELH','QVOBS', 'WOBS','UOBS','VOBS', 'THETAV', 'TABS']

c1=(-20.0,20.0,21,'[%]'   )
c2=(-1.0,1.0  ,21,'[g/kg]')
c3=(-1.0,1.0  ,21,'[m/s]' )
c4=(-3.0,3.0  ,21,'[m/s]' )
c5=(-1.0,1.0  ,21,'[m/s]' )
c6=(-2.0,2.0  ,21,'[K]'   )
c7=(-2.0,2.0  ,21,'[K]'   )

contour     =[
              c1,c2,c3,c4,c5,c6,c7
              #c2,c2,c2,c2,c2,c2,c2
             ]


var_to      =  [
                    1,1,100,1,1, 1,1  
                    #1,1,1,1,1, 1,1  
               ]

alt         =  [
                3.5, 3.5, 3.5,
                3.5, 3.5, 3.5,
                3.5
               ]

co1='RdBu_r'

color       =  [
                co1,co1,co1,
                co1,co1,co1,
                co1,co1,co1
               ]

####bar ,y axis, top_lfc_pbl,cm a mais do grafico
a1          =  (True,False,False,0.35,1.28)
axis_on     =  [a1,a1,a1,a1,a1,a1,a1]


show       =  [
#                True,True,True,
#                True,True,True,
                False,False,False,
                False,False,False,
                False,False,False,
              ]

days        = [ 
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
                [(2014,1,1,6),(2014,1,1,18)],
            ]


#plot2d_im_diff(ex1,ex2,variables,days=[],alt=[],explabel=[],var_to=[],contour=[],axis_on=[],show=[]):
two.plot2d_im_diff(exp1,exp2,var,alt=alt,days=days,color=color,explabel=exp_label,var_to=var_to,contour=contour,axis_on=axis_on,show=show)


