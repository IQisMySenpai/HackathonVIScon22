import jwt

token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6WkdEaEVRa3hBZFRvRGZyd0hZcmlRMkpCYmVibUxHMXkyUldYRzN3bl9nIn0.eyJleHAiOjE2NjU4NTA0NDUsImlhdCI6MTY2NTg0Njg0NiwiYXV0aF90aW1lIjoxNjY1ODQ2ODQ1LCJqdGkiOiI3NDc1MmJjMS04NTM1LTQyYzItYTZiOS0yMjMzZmRiZTZkNzciLCJpc3MiOiJodHRwczovL2F1dGgudnNldGguZXRoei5jaC9hdXRoL3JlYWxtcy9WU0VUSCIsImF1ZCI6InZzZXRoLXRlYW0tMTEiLCJzdWIiOiI1ZmYzYWNiOC01NWIwLTQ0ZWItYjk5Yy0zMWU1MGIyMWQwNWIiLCJ0eXAiOiJJRCIsImF6cCI6InZzZXRoLXRlYW0tMTEiLCJub25jZSI6ImRmw7ZsYXNkZsO2bGFzZGpkZiIsInNlc3Npb25fc3RhdGUiOiIwY2I3YTc5NC05YWU4LTRhNjktODI3NS04YTAwZjNiZTgyM2UiLCJhY3IiOiIxIiwic2lkIjoiMGNiN2E3OTQtOWFlOC00YTY5LTgyNzUtOGEwMGYzYmU4MjNlIiwicmVzb3VyY2VfYWNjZXNzIjp7InZtcF9wcm9kX3ZtcHNpdGVfdm1wc2l0ZSI6eyJyb2xlcyI6WyJ2c2V0aC1taXRnbGllZCJdfSwidmlzLXdlYnNpdGUiOnsicm9sZXMiOlsidmlzLW1lbWJlci1vcmRpbmFyeSIsInZzZXRoLW1lbWJlciJdfSwidnNldGgtaGVsZmVydG9vbCI6eyJyb2xlcyI6WyJsb2dpbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwibmFtZSI6IkFsZXhhbmRlciBTb3RvdWRlaCIsInByZWZlcnJlZF91c2VybmFtZSI6ImFzb3RvdWRlaCIsImdpdmVuX25hbWUiOiJBbGV4YW5kZXIiLCJmYW1pbHlfbmFtZSI6IlNvdG91ZGVoIn0.Noi7lrTRgwk69kuM52TMonN_irzbpvCR-m_KvR28Hg16TF7xmB1a4w_0KDrQJzLLEttnFB7ohuJvP5k54LqRwIsKNixlrQL9GbgwLMXcA5qdGmwtOiML141yXF4fAxm9YBkdmvqrRxc4i495zFZcz3RaJQJVaJ8F7P7mI7nBHyNBvhu0HiAXQJ5gFTxw32Sa4USyaFKOmz5e8To_Pg1AJmPOvXr3na6C3TdPE7SjUY7-VmMBC4-aq1ywnZEqOvgNWaXr-orVzpIV6TVQAKQHTFcFeyY1QLW0XHF8EZQHptv0wNWc_-ssZ1wwHY6ZEsvkDLHZkd6YhH_61JFsb92P3A"

key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtP+L+6HuC6g/d6xJxjdS\ngTMYusm9HehmbfB/NKbjKPBVQ7ebnoMuvPDI8MMRsQS4/vx5bdkofxD1qresiCJu\nkBFZoZ25r7/WyPLv09VgaHiwevO+Ygy7pb2aySO9ByDrWTfwj2mN4N80GyNXJbH4\n52vYXNdETPmBpawEp5O4uRs08tqxMYq0C4mWSTnAWZazuijmfA0FXUi7juVUEqtq\nfJYGMWtj5nEOhjvv3u7uNpMPRjz/pk+Ffb+qQZ6PBymCx+jrBm1ThEtRAeSEauXl\nxHvsfsCEt8fAr1YUR9Xu/16VbA/phZ5gzSrv8D+wdFdEB4BqvI0PpR1TJHzvdD82\nJQIDAQAB\n-----END PUBLIC KEY-----\n'


res = jwt.decode(jwt=token, key=key, algorithms=["RS256"], options={"verify_aud": False})
print(res)
# def verify_user(id_token: str)

