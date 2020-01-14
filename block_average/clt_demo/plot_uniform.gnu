set encoding iso_8859_1
set terminal postscript solid color enhanced "Helvetica, 30"
set output "|ps2pdf - ./tmp.pdf"

name="fig_uniform.pdf"
margins="5"

step(x) = abs(x) < 0.94 ? 0.5 : 1/0

set xlabel "x" font ",36" offset 0,-0.5
set ylabel "f(x)" font ",36"

set mxtics 2
set mytics 5

set xtics 1 font ",30"
set ytics 0.25 font ",30"

set samples 1000
unset key

p[-2:2][0:1]\
step(x) w l lw 5 lc rgb "blue",\
"<echo '-0.99 0.5'" w p pt 65 ps 2 lw 5 lc rgb "blue",\
"<echo '0.99 0.5'" w p pt 65 ps 2 lw 5 lc rgb "blue"

unset output
!pdfcrop.pl ./tmp.pdf ./@name --margins @margins
!rm -f ./tmp.pdf

