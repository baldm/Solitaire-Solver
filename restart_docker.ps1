docker ps -q | % { docker stop $_ }
docker system prune -a --volumes -f
docker-compose up -d