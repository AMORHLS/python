FROM java:8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
VOLUME /tmp
ADD ehr-profile.jar ehr-profile.jar
RUN bash -c 'touch /ehr-profile.jar'
EXPOSE 9051
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/ehr-profile.jar"]
