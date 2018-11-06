USAGE="USAGE: $0 <Target-NS>"

if [ $# -eq 0 ]; then
    echo "ERROR: Provide Target NetScaler IP Address"
    echo $USAGE
    exit
elif [ $# -gt 1 ]; then
    echo "ERROR: Too many arguments"
    echo $USAGE
    exit
fi


TARGET_NS=$1



CURR_DIR=`dirname $0`

echo `ls $CURR_DIR`

FILES_TO_TRASNFER="$CURR_DIR/error.html  $CURR_DIR/error.xml  $CURR_DIR/error.xsd  $CURR_DIR/sample_sign.xml  $CURR_DIR/sample.wsdl"

scp $FILES_TO_TRASNFER nsroot@$TARGET_NS:/var/tmp/

echo "Required files copied to $TARGET_NS"
