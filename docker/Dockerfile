FROM registry.gitlab.com/cyb3r-jak3/alpine-pandas:3.9

WORKDIR /usr/src/app
COPY ../MetaStalk ./metastalk
COPY .. ./
RUN apk add --no-cache libffi-dev gcc musl-dev make build-base libstdc++
RUN pip --disable-pip-version-check --no-cache-dir install  . && \
    rm -rf requirements.txt requirements-dev.txt README.md
RUN apk del libffi-dev gcc musl-dev make build-base

EXPOSE 8052

ENV HOST=0.0.0.0
VOLUME ["/photos"]
ENTRYPOINT ["metastalk"]
CMD [ "--no-open", "/photos"]
