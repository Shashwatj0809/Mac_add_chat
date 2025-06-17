# 🖧 MAC-Based LAN Chat Application

## Secure LAN Chat with MAC Address Filtering

This project enables a **LAN-based chat system** where only **whitelisted devices** (identified by their **MAC addresses**) are allowed to connect and participate in real-time messaging.

---

## 📌 Features

-  Restricts access to allowed MAC addresses only.
-  Real-time messaging via sockets within a local network.
-  Terminal-based Python client & server.
-  Optional web-based frontend with WebSocket support (via Flask-SocketIO).
-  Loopless topology — supports 1:N communication within a LAN.

---

##  Architecture

###  High-Level Overview

```txt
┌──────────────┐        ┌────────────────┐        ┌──────────────┐
│  Client 1    │  --->  │                │  --->  │  Client 2    │
│ (Allowed MAC)│        │    Server.py   │        │ (Allowed MAC)│
└──────────────┘        │ (TCP Socket or │        └──────────────┘
                        │  Flask-SocketIO)│
                        └────────────────┘
                               ▲
                               │
                      allowed.txt (MAC Filter List)
