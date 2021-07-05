
target "default" {
  dockerfile = "./docker/Dockerfile"
  context = "."
  tags = [
    "cyb3rjak3/metastalk:latest",
    "registry.gitlab.com/cyb3r-jak3/metastalk:latest",
    ]
}

target "platforms" {
  platforms = [
    "linux/amd64",
    "linux/arm/v6",
    "linux/arm/v7",
    "linux/arm64",
    "linux/386",
  ]
}

target "release" {
  inherits = ["default", "platforms"]
}