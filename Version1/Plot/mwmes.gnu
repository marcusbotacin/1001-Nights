set encoding utf8
set terminal postscript eps color colortext
set xdata time
set timefmt "%s"
set output "mwmes.eps"
set grid
set xtics 1
set title "Collected Samples X Month"
plot "monthlymw-2012.dat" using 0:2:xtic(1) title "2012" lw 3 with lines, "monthlymw-2013.dat" using 0:2:xtic(1) title "2013" lw 3 with lines, "monthlymw-2014.dat" using 0:2:xtic(1) title "2014" lw 3 with lines, "monthlymw-2015.dat" using 0:2:xtic(1) title "2015" lw 3 with lines
