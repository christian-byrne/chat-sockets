Sockets practice for cloud computing course.

### References

- [tcp - Linux Man Page](https://man7.org/linux/man-pages/man7/tcp.7.html)
- [Python socket docs](https://docs.python.org/3/library/socket.html)
- [Python Bytes Object docs](https://docs.python.org/3/c-api/bytes.html)
- [Custom Procols for variable payload size](https://stackoverflow.com/questions/1708835/python-socket-receive-incoming-packets-always-have-a-different-size)
- [Standard Streams - GNU](https://www.gnu.org/software/libc/manual/html_node/Standard-Streams.html)
- [How to tell if a connection is dead in python](https://stackoverflow.com/questions/667640/how-to-tell-if-a-connection-is-dead-in-python)


### Associated Commands

<details>
    <summary>Expand</summary>

- Print PID of process by name

```bash
pidof process
```

- Kill process by name

```bash
pkill process
```

- Print PID of process bound on port 8080

```bash
fuser 8080/tcp
lsof -i:8080
```

- Kill process bound on port 8080

```bash
fuser -k 8080/tcp
kill -9 $(lsof -t -i:8080)
npx kill-port 8080
tcpkill -i eth0 host xxx.xxx.xxx.xxx and port yyyy
```
</details>


