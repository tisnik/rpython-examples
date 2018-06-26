width="2048"

OUTFILE="ansi_c_linear_scale.times"
PREFIX="ansi_c_linear_scale"

rm $OUTFILE

for height in $(seq 0 100 3500)
do
    echo "${width} x ${height}"
    echo -n "${height} " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" ./mandelbrot $width $height 255 > "${PREFIX}_${width}_${height}.ppm"
done
