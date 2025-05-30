Build the docker image (this only needs to do once and can take some time).
```shell
./build_docker_image.sh
```

For detached mode (default):
```shell
./start_docker.sh
```

For interactive mode:
```shell
./start_docker.sh -i
```

To stop:
```shell
./stop_docker.sh
```

To exec explicitly:
```shell
./enter_docker.sh
```
