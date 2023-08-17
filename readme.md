Homepage Link : www.korcat.inha.ac.kr

%% Begin Waypoint %%
- **[[KorCAT-web V3]]**

%% End Waypoint %%

--- 

## NGINX 

### Configure Settings 

```shell
sudo vi /etc/nginx/sites-available/korcat
```

```nginx
server {
    listen 3000;
    server_name 165.246.44.247;  # Change this to your domain or server IP

    location /api {
        proxy_pass http://127.0.0.1:8000;  # FastAPI backend
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        proxy_pass http://127.0.0.1:3030;  # React front-end
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```shell
sudo ln -s /etc/nginx/sites-available/korcat /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
```

```shell
sudo nginx -t
```

### Reload & Check Status 

```shell
sudo systemctl reload nginx
sudo systemctl status nginx
```

--- 

## BACKEND 

- location: `/kocat/backend` 
- environment; `/korcat/backend/.env/`

### Server Maintenance 

#### Run 2 Uvicorn Workers w/ Gunicorn In Background

```shell
nohup python -m gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app > gunicorn.log 2>&1 &
disown
```

#### Logs & Kill Server

- Check for logs in `/korcat/backend/gunicorn.log` 
- Run `sudo kill -9 [PID]` for all running uvicorn & gunicorn workers 

##### Example `gunicorn.log`

```
[2023-08-11 11:10:49 +0000] [50052] [INFO] Starting gunicorn 21.2.0
[2023-08-11 11:10:49 +0000] [50052] [INFO] Listening at: http://0.0.0.0:8000 (50052)
[2023-08-11 11:10:49 +0000] [50052] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2023-08-11 11:10:49 +0000] [50055] [INFO] Booting worker with pid: 50055
[2023-08-11 11:10:49 +0000] [50056] [INFO] Booting worker with pid: 50056

[2023-08-11 11:11:18 +0000] [50055] [INFO] Started server process [50055]
[2023-08-11 11:11:18 +0000] [50056] [INFO] Waiting for application startup.
[2023-08-11 11:11:18 +0000] [50055] [INFO] Waiting for application startup.
[2023-08-11 11:11:18 +0000] [50055] [INFO] Application startup complete.
[2023-08-11 11:11:18 +0000] [50056] [INFO] Application startup complete.
```

```shell
sudo kill -9 50052 50055 50055
```

#### Confirm Server 

```shell
sudo netstat -lpn | grep :'8000'
```

--- 

## FRONTEND 

- location: `/korcat/frontend` 

### Run Test Server

```shell
npm start
```

### Update Static Build 

```shell
npm run build
serve -s build
```

- building the static server will automatically update frontend code
	- no need for re-run

### Start Build Server In Background 

```shell
nohup sh -c 'serve -s build -l 3030 </dev/null >/dev/null 2>&1' &
disown
```

#### Confirm Server 

```shell
sudo netstat -lpn | grep :'3030'
```

--- 
