ps -aux | grep python3|xargs kill -9
nohup python3 /django/update/manage.py runserver 0.0.0.0:5001 > djo.out 2>&1 &
