set terminal postscript eps color colortext
set key outside
set encoding utf8
set auto x
set auto y
set logscale y
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set output "variants2.eps"
set grid
set title "Cluster Size X # of Samples"
plot "variants2.dat" using 2:xtic(int($0)%3==1 ? strcol(1):'') with boxes ls 1 title "\# of Samples"
