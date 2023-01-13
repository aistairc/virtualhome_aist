FROM ubuntu:22.04
ENV LANG C.UTF-8
RUN apt-get update && apt-get install -y --no-install-recommends \
                xvfb
COPY ./run_sim.sh /
RUN chmod +x /run_sim.sh

RUN apt-get update && apt-get -y upgrade

# port 8080 is the port used in in Editor training.
EXPOSE 8080

ENTRYPOINT ["/run_sim.sh"]