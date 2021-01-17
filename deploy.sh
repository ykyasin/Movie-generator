docker rm -f $(docker ps -a -q)
docker rmi frontend_service_image
docker rmi location_service_image
docker rmi weather_service_image
docker rmi movie_service_image
docker network prune -f
docker build -t frontend_service_image service_1
docker build -t location_service_image service_2
docker build -t weather_service_image service_3
docker build -t movie_service_image service_4
docker network create network1
docker run -d -p 5000:5000 --network network1 --name frontend_service frontend_service_image
docker run -d --network network1 --name location_service location_service_image
docker run -d --network network1 --name weather_service weather_service_image
docker run -d --network network1 --name movie_service movie_service_image
