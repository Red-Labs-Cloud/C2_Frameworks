# Command and Control Infrastructure
Unveiling the secret weapon of cyber attackers. This series explores Command & Control, the nerve center of online threats. Learn how attackers control your systems & how to defend your organization.


## Deploy the Infrastructure


### Prepare Local Environment
Clone the Repo
```console
rfs@debian:~$ git clone https://github.com/Red-Labs-Cloud/C2_Infrastructure.git
```

Enter the new folder

```console
rfs@debian:~$ cd C2_Infrastructure
```
Install all Necessary packages on our local machine.

```console
rfs@debian:~/C2_Infrastructure$ sudo ./install.py
```
Our base machine is ready to deploy any lab locally or Cloud.

## Command Help

```console
rfs@debian:~$ redlabs --help

redlabs --help
redlabs --install
redlabs --config

- c2-cs
- c2-mythic

redlabs --local

- Vmware
- ProxMox
- Linux Box (Any)

```

## C2 Servers


## Install Locally




## Install

```console
rfs@debian:~$ redlabs --install
```

```console
rfs@debian:~$ redlabs --config web --local
```

## Install a Cobalt Strike C2 Locally

```console
rfs@debian:~$ redlabs --install c2-cs --local
```

## Config a Cobalt Strike C2 Locally
```console
rfs@debian:~$ redlabs --config c2-cs
```

## Cloud Install
```console
rfs@debian:~$ redlabs --config web --aws
```
