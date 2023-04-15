# net-deauth

Ağdaki cihazı paketler göndererek ağdan düşürmek için kullanılır.

## Gereksinimler

net-deauth aşağıdaki kütüphaneleri kullanır.

* Colorama
* Scapy

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/net-deauth.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| target    | Hedef cihazı belirtmek için kullanılır. |
| gateway   | Ağ geçidini belirtmek için kullanılır. |
| -c        | Paket adetini belirtmek için kullanılır. Eğer belirtilmezse program çalıştığı boyunca paket gönderilir. |
| -t        | Paket gönderim süresini belirtmek için kullanılır. |
| -i        | Saldırı için kullanılacak ağ arayüzünü belirtmek için kullanılır. |

```bash
usage: net-deauth.py [-h] [-c C] [-t T] [-i I] target gateway

positional arguments:
  target      Target MAC
  gateway     Target Gateway

options:
  -h, --help  show this help message and exit
  -c C        Count
  -t T        Interval
  -i I        Interface
```

## Örnekler

```python
python3 net-deauth.py TARGET_IP GATEWAY -c 50 -t 1 -i wlan0mon
python3 net-deauth.py TARGET_IP GATEWAY -t 1 -i wlan0mon
```
