set -e
mkdir -p converted
for x in $(find . -name '*.wp');
do 
    echo "Converting $x"

    meta=$(dirname $x)/$(basename $x .wp).meta
    
    pandoc \
    --from=html \
    --to=rst \
    --normalize \
    --reference-links \
    --output=converted/$(basename $x .wp).rst \
    --template=/home/mariano/Blog/site/wordpress/pandoc_template.rst \
    --variable="title:$(cat $meta | head -n 1 | tail -n 1 | sed -r 's/^\.\. [a-z]+: (.*)/\1/')" \
    --variable="slug:$(cat $meta | head -n 2 | tail -n 1 | sed -r 's/^\.\. [a-z]+: (.*)/\1/')" \
    --variable="date:$(cat $meta | head -n 3 | tail -n 1 | sed -r 's/^\.\. [a-z]+: (.*)/\1/')" \
    --variable="tags:$(cat $meta | head -n 4 | tail -n 1 | sed -r 's/^\.\. [a-z]+: (.*)/\1/')" \
    $x;
done
