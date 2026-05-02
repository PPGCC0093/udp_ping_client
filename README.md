# UDP Ping Client

A simple UDP ping client written in Python. The script sends 10 UDP packets to a
server, waits up to 1 second for each response, then prints packet loss and RTT
statistics.

## Requirements

- Python 3.13 or compatible Python 3 version
- A UDP server listening on `127.0.0.1:12000`
- Docker, if you want to run the client in a container

## Running Locally

Start your UDP server first, then run:

```bash
python server.py
```

The client sends messages in this format:

```text
ping 1
ping 2
...
ping 10
```

For each received response, it prints the response text and round-trip time.
Timeouts are reported as lost packets.

## Running With Docker

Build the image:

```bash
docker build -t udp-ping-client .
```

Run the container:

```bash
docker run --rm udp-ping-client
```

Because the script connects to `127.0.0.1`, Docker users usually need host
networking when the UDP server is running on the host machine:

```bash
docker run --rm --network host udp-ping-client
```

Host networking is supported on Linux. On Docker Desktop, change `SERVER_HOST`
in `server.py` to the appropriate host address, such as `host.docker.internal`.

## Configuration

The connection settings are defined at the top of `server.py`:

```python
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12000
```

Edit those values if your UDP server is running on a different host or port.

## Output

At the end of the run, the client prints:

- packets sent
- packets received
- packets lost
- packet loss percentage
- average RTT, when at least one response is received
