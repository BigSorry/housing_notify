## Telegram notification for rentals


### Remainder for w11 docker test pi5

### Build the image

```bash
docker buildx build --platform linux/arm64 -t {build_name}:latest .
```

### Run image
```bash
docker run --platform linux/arm64 {build_name}:latest
```

