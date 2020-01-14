set encoding iso_8859_1
set terminal postscript dashed color enhanced "Helvetica, 30"
set output "|ps2pdf - ./tmp.pdf"

name="fig_avgdist.pdf"
margins="5"

normal(x,mu,sig) = 1./(sig*sqrt(2.*pi))*exp(-0.5*((x-mu)/sig)**2)

set xlabel "x" font ",36" offset 0,-0.5
set ylabel "f(x)" font ",36"

set mxtics 2
set mytics 5

set xtics 1 font ",30"
set ytics 1 font ",30"

set samples 1000

p[-2:2][:2.5]\
'uniform.out' u 1:2 w l lw 6 dt 1 title "N=3",\
'uniform.out' u 1:3 w l lw 6 dt 1 title "N=5",\
'uniform.out' u 1:4 w l lw 6 dt 1 title "N=10",\
normal(x,0.0,1./(sqrt(3)*sqrt(3))) lw 4 dt 2 lc rgb "black" notitle,\
normal(x,0.0,1./(sqrt(3)*sqrt(5))) lw 4 dt 2 lc rgb "black" notitle,\
normal(x,0.0,1./(sqrt(3)*sqrt(10))) lw 4 dt 2 lc rgb "black" notitle

unset output
!pdfcrop.pl ./tmp.pdf ./@name --margins @margins
!rm -f ./tmp.pdf

