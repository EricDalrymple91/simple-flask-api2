# Simple Flask App

# Usage

```
python app/app.py
```

# Docker Usage

```
docker build --tag thisimg .
docker push thisimg
docker run --env-file .env -p 8080:8080 thisimg:latest
docker run --entrypoint '' -ti thisimg /bin/bash
```
