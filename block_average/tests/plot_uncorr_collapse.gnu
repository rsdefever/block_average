set encoding iso_8859_1
set terminal postscript solid color enhanced "Helvetica, 30"
set output "|ps2pdf - ./tmp.pdf"

name="fig_uncorr_collapse.pdf"
margins="5"

set xlabel "Number blocking ops" font ",36" offset 0,-0.5
set ylabel "Distribution Variance" font ",36"

set mxtics 2
set mytics 2

#set xtics 1 font ",30"
#set ytics 1 font ",30"

set key horizontal outside top

p[][]\
'uncorr_n250000_blkavg.out'  u 1:($3*250000):($4*250000) w yerrorbars lw 6  pt 6 ps 2 title "N=250,000",\
'uncorr_n500000_blkavg.out'  u 1:($3*500000):($4*500000) w yerrorbars lw 6  pt 6 ps 2 title "N=500,000",\
'uncorr_n1000000_blkavg.out' u 1:($3*1000000):($4*1000000) w yerrorbars lw 6 pt 6 ps 2  title "N=1,000,000",\
'uncorr_n2000000_blkavg.out' u 1:($3*2000000):($4*2000000) w yerrorbars lw 6 pt 6 ps 2  title "N=2,000,000",\
'uncorr_n4000000_blkavg.out' u 1:($3*4000000):($4*4000000) w yerrorbars lw 6 pt 6 ps 2  title "N=4,000,000"

unset output
!pdfcrop.pl ./tmp.pdf ./@name --margins @margins
!rm -f ./tmp.pdf

