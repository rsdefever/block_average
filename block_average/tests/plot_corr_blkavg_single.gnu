set encoding iso_8859_1
set terminal postscript solid color enhanced "Helvetica, 30"
set output "|ps2pdf - ./tmp.pdf"

name="fig_corr_blkavg_single.pdf"
margins="5"

set xlabel "Number blocking ops" font ",36" offset 0,-0.5
set ylabel "Variance of average" font ",36"

set mxtics 2
set mytics 2

#set xtics 1 font ",30"
#set ytics 1 font ",30"

set key horizontal outside top

p[][0:0.002]\
'corr_n250000_blkavg.out' u 1:3:4 w yerrorbars lw 6  pt 6 ps 2 title "N=250,000"

unset output
!pdfcrop.pl ./tmp.pdf ./@name --margins @margins
!rm -f ./tmp.pdf

