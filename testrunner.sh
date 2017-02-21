export PYTHONPATH=./src
MODULE=pyfuckery
HTML_DIR=./htmlcov
INDEX=$HTML_DIR/index.html

if [ -e $HTML_DIR ]; then
    echo "Removing existing coverage reports."
    rm -rf $HTML_DIR
fi

pytest -s -v --cov-report=html --cov $MODULE --no-print-logs $1

if [ -e $INDEX ]; then
    echo "Opening coverage report."
    open $INDEX
fi
