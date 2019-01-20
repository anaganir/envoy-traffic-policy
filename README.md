# Build containers

docker build -t front front; docker build -t front-envoy envoy-front; docker build -t hello-envoy envoy; docker build -t hello retry/

# Run the containers

docker run -d --name envoy_container -it --net=bridge -p 3451:3451 -p 4321:4321 hello-envoy ; sleep 1; docker run -d --name redis -it --net=bridge redis:latest; sleep 1;docker run -e PORT=80 -e STATE=Ok -d --name hello_container-1 -it --net=bridge hello; docker run -e PORT=90 -e STATE=Ok -d --name hello_container-2 -it --net=bridge hello; docker run -e PORT=100 -e STATE=Ok -d --name hello_container-3 -it --net=bridge hello; docker run -e PORT=110 -e STATE=Ok -d --name hello_container-4 -it --net=bridge hello; docker run -e PORT=120 -e STATE=Ok -d --name hello_container-5 -it --net=bridge hello; docker run -e PORT=80 -e SLEEP=5 -d --name front_container-1 -it --net=bridge front; sleep 1; docker run -d --name front_envoy_container -it --net=bridge -p 1234:1234 front-envoy

# Destroy containers

docker rm -f hello_container-1; docker rm -f redis; docker rm -f envoy_container; docker rm -f hello_container-2; docker rm -f hello_container-3; docker rm -f hello_container-4; docker rm -f hello_container-5; docker rm -f front_container-1; docker rm -f front_envoy_container
