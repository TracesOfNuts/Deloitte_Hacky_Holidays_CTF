![challenge](./img/Capture.PNG)

#### CHALLENGE INFORMATION

Santa sent a present to all the good boys and girls, can you figure out what he sent?

*Author information: This challenge is developed by Deloitte.*

#### FILES

You will need the files below in order to solve this challenge.

[dump.pcap](./img/dump.pcap)

#### (50 Points) PRESENT DROP

Santa sent a present to all the good boys and girls, can you figure out what he sent?

---

#### (Solution) PRESENT DROP

- Open the file using Wireshark.
- Scroll down to item 58.
- Right-click on the `Portable Network Graphics`
- Click on `Export Packet Bytes..`
- Save as [flag.png](./img/flag.png)
- Open image

![flag](./img/flag.png)

Flag:

```
CTF{HAPPY_HOLIDAYS}
```

