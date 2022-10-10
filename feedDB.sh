#!/bin/bash

#python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db init
#python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db migrate
#python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db upgrade

#source venv/bin/activate 
#export FLASK_ENV=development 


while getopts 'obise:' OPTION; do
  case "$OPTION" in
    e)
        python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db init
        python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db migrate
        python3 /home/herman/Documents/nicvi-linux/ioet/ioet-intern-tests/python-pizza-planet-hp/manage.py db upgrade

        source venv/bin/activate 
        export FLASK_ENV=development 
        echo "init"
        ;;
    o)
        for o in {1..10}
        do 
        curl --location --request POST 'http://127.0.0.1:5000/order/' \
        --header 'Access-Control-Allow-Origin: *' \
        --header 'Server: Werkzeug/2.0.2 Python/3.10.5' \
        --header 'Content-Type: application/json' \
        --data-raw '{"client_name": "client-'"$o"'", "client_dni": "3234", "client_address": "Santa Rosa y 10ma Norte", "client_phone": "0969618162", "size_id": "1", "ingredients": ["1", "2","3"], "beverages": ["1", "2"]}'
        done
        echo "order created"
        ;;
    b)
        for j in {1..10}
        do 
        curl --location --request POST 'http://127.0.0.1:5000/beverage/' \
        --header 'Access-Control-Allow-Origin: *' \
        --header 'Server: Werkzeug/2.0.2 Python/3.10.5' \
        --header 'Content-Type: application/json' \
        --data-raw '{"name": "beverage-'"$j"'", "price": "'"$j"'"}'
        done
        echo "bebverage created"
        ;;
    i)
        for i in {1..10}
        do 
            curl --location --request POST 'http://127.0.0.1:5000/ingredient/' \
            --header 'Access-Control-Allow-Origin: *' \
            --header 'Server: Werkzeug/2.0.2 Python/3.10.5' \
            --header 'Content-Type: application/json' \
            --data-raw '{"name": "ingredient-'"$i"'", "price": "'"$i"'"}'
        done
        echo "ingredient created"
        ;;
    s)
        for k in {1..10}
        do 
        curl --location --request POST 'http://127.0.0.1:5000/size/' \
        --header 'Access-Control-Allow-Origin: *' \
        --header 'Server: Werkzeug/2.0.2 Python/3.10.5' \
        --header 'Content-Type: application/json' \
        --data-raw '{"name": "size-'"$k"'", "price": "'"$k"'"}'
        done
        echo "size created"
        ;;
    ?)
      echo "script usage: $(basename \$0) [-l] [-h] [-a somevalue]" >&2
      exit 1
      ;;
  esac
done
