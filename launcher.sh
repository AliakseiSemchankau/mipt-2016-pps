#!/bin/bash

export PYTHONPATH=$PWD
export CONF=$PWD/conf

case $1 in
    system)
        exec python system/run.py $CONF
        ;;
    scheduler)
        exec python scheduler/run.py $CONF
        ;;
    frontend)
        exec python order/flask/run.py $CONF
        ;;
    algorithm)
        exec python algorithm/run.py $CONF
        ;;
    all)
        python algorithm/run.py $CONF &
        python order/flask/run.py $CONF &
        python scheduler/run.py $CONF &
        python system/run.py $CONF &
        ;;
esac

