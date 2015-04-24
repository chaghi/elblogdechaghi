for x in converted/*.rst;
do
    echo $x
    sed -i.bak -r 's/\|IMG\\_/\|IMG_/' "$x"
done
