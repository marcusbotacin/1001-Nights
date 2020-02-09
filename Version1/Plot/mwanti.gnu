set terminal postscript eps color colortext
set encoding utf8
set auto x
set yrange [0:70]
set ytics 10
set format y '%2.0f%%'
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set output "mwanti.eps"
set grid
set title "Sample Distribution (%) X Obfuscation Technique"
plot "mwanti.dat" using 2:xtic(1) ti col, '' u 3 ti col, '' u 4 ti col, '' u 5 ti col
