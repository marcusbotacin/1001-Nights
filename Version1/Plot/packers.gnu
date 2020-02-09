set terminal postscript eps color colortext
set auto x
set yrange [0:100]
set ytics 10
set output "mwpacker.eps"
set grid
set title "Porcentagem de exemplares X Packer"
plot "packers2012.dat" using (column(0)):2:xtic(1) title "2012" lw 3 with lines
