set terminal postscript eps color colortext
set auto x
set encoding utf8
set yrange [0:80]
set ytics 10
set format y '%2.0f%%'
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set output "mwtype.eps"
set grid
set title "Sample distribution (%) vs. filetype"
plot "mwtype.dat" using 2:xtic(1) ti col, '' u 3 ti col, '' u 4 ti col, '' u 5 ti col
