#!/usr/bin/env bash
set -ex
command="docker buildx bake release --file ./docker/docker-bake.hcl --set *.cache-to=type=local,dest=./.buildx-cache --set *.cache-from=type=local,src=./.buildx-cache"
if [[ "$CI_COMMIT_TAG" =~ /^v\d+.\d+.\d+/ ]]; then
  echo "$DOCKER_TOKEN" | docker login -u "$USER" --password-stdin
  echo "$CI_REGISTRY_PASSWORD" | docker login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"
  command+=" --push"
fi
$command