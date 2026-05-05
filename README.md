# UDP Ping Client

A small Python UDP ping client for measuring round-trip time and packet loss
against a UDP echo server.

The current entrypoint is `udp_ping_clien.py`. Despite the filename, it acts as the
client: it sends 10 UDP packets, waits up to 1 second for each response, and
prints basic statistics at the end.

## Requirements

- Python 3.13 or newer
- A UDP server listening on `127.0.0.1:12000`
- Docker, optional
- uv, optional

This project has no third-party Python dependencies.

## Run Locally

Start your UDP server first, then run the client:

```bash
python udp_ping_clien.py
```

If you use uv:

```bash
uv run python udp_ping_clien.py
```

The client sends these messages:

```text
ping 1
ping 2
...
ping 10
```

Each successful response prints the response text and RTT in milliseconds.
Timeouts are counted as lost packets.

## Run With Docker

Build the image:

```bash
docker build -t udp-ping-client .
```

Run the image:

```bash
docker run --rm udp-ping-client
```

When the UDP server is running on the host machine, use host networking on
Linux so `127.0.0.1` resolves to the host network namespace:

```bash
docker run --rm --network host udp-ping-client
```

On Docker Desktop, host networking may not behave the same way. In that case,
change `SERVER_HOST` in `udp_ping_clien.py` to the correct host address, commonly
`host.docker.internal`.

## Configuration

Connection settings are defined near the top of `udp_ping_clien.py`:

```python
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12000
```

Update these values if your UDP server uses a different host or port.

## Output

After all packets are sent, the client prints:

- packets sent
- packets received
- packets lost
- packet loss percentage
- average RTT, if at least one response was received

## Docker Image Workflow

The repository includes a GitHub Actions workflow at
`.github/workflows/docker-image.yml`. It builds the Docker image on pull
requests and publishes signed images to GitHub Container Registry for configured
branches and tags.
