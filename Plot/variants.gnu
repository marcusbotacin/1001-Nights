set terminal postscript eps color colortext
set key outside
set encoding utf8
set auto x
set auto y
set ytics 5
set format y '%2.0f%%'
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set output "variants.eps"
set grid
set title "Sample Variants (%) X Matching Threshold"
plot "variants.dat" using 2:xtic(1) ti col
