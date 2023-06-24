FROM ubuntu:22.04
ENV LANG C.UTF-8
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y --no-install-recommends \
    xvfb

# setup unity exe
RUN apt install -y unzip
RUN mkdir -p /unity_vol/executable_unix
# aistairc/virtualhome_unity_aist へのアクセス権限が必要なので
# https://github.com/aistairc/virtualhome_unity_aist/releases/download/Door_Modified_Build_2023_0404/Modified_Camera_Build_Linux.zip を事前にダウンロードしておく
COPY Door_Modified_Build_2023_0404/Modified_Camera_Build_Linux.zip /tmp/.
RUN unzip -d /tmp /tmp/Door_Modified_Build_2023_0404/Modified_Camera_Build_Linux.zip
RUN cp -r /tmp/Modified_Camera_Build_Linux/* /unity_vol/executable_unix
RUN chmod +x /unity_vol/executable_unix/Door_Modified_Build_2023_0404/Modified_Camera_Build_Linux.x86_64

COPY ./run_sim.sh /
RUN chmod +x /run_sim.sh

# port 8080 is the port used in in Editor training.
EXPOSE 8080

ENTRYPOINT ["/run_sim.sh"]
