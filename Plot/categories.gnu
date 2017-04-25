set terminal postscript eps color colortext
set auto x
set encoding utf8
set yrange [0:18]
set ytics 0.5
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set output "categories.eps"
set grid
set title "Categories"
plot "categories.dat" using 3:xtic(1) ti col
