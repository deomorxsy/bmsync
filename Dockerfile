FROM python:3-slim AS build-env
COPY . /bmsync/
WORKDIR /bmsync/

FROM gcr.io/distroless/python3
COPY --from=build-env /app/* ./bmsync/build-env/
WORKDIR /bmsync/
CMD ["./app/server/serverDiscovery.py"]


