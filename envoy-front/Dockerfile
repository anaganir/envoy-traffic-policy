FROM envoyproxy/envoy:latest
RUN apt-get update; apt-get install -y curl; apt-get install -y net-tools; apt-get install -y procps; apt-get install -y vim
COPY envoy.yaml /etc/envoy/envoy.yaml
EXPOSE 3451
CMD /usr/local/bin/envoy -c /etc/envoy/envoy.yaml -l debug
