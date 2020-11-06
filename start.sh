ps -aux | grep python3|xargs kill -9
nohup python3 /root/django/manage.py runserver 0.0.0.0:8082 > djo.out 2>&1 &
