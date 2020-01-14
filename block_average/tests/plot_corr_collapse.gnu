set encoding iso_8859_1
set terminal postscript solid color enhanced "Helvetica, 30"
set output "|ps2pdf - ./tmp.pdf"

name="fig_corr_collapse.pdf"
margins="5"

set xlabel "Number blocking ops" font ",36" offset 0,-0.5
set ylabel "Variance of distribution" font ",36"

set mxtics 2
set mytics 2

#set xtics 1 font ",30"
#set ytics 1 font ",30"

set key horizontal outside top

p[][]\
'corr_n250000_blkavg.out'  u 1:($3*250):($4*250)  w yerrorbars lw 6  pt 6 ps 2 title "N=250,000",\
'corr_n500000_blkavg.out'  u 1:($3*500):($4*500)  w yerrorbars lw 6  pt 6 ps 2 title "N=500,000",\
'corr_n1000000_blkavg.out' u 1:($3*1000):($4*1000) w yerrorbars lw 6 pt 6 ps 2  title "N=1,000,000",\
'corr_n2000000_blkavg.out' u 1:($3*2000):($4*2000) w yerrorbars lw 6 pt 6 ps 2  title "N=2,000,000",\
'corr_n4000000_blkavg.out' u 1:($3*4000):($4*4000) w yerrorbars lw 6 pt 6 ps 2  title "N=4,000,000"

unset output
!pdfcrop.pl ./tmp.pdf ./@name --margins @margins
!rm -f ./tmp.pdf

