# Command and Control Infrastructure
Unveiling the secret weapon of cyber attackers. This series explores Command & Control, the nerve center of online threats. Learn how attackers control your systems & how to defend your organization.


## Deploy the Infrastructure


### Clone the Repo

```console
rfs@debian:~$ git clone https://github.com/Red-Labs-Cloud/C2_Infrastructure.git
```

```console
rfs@debian:~$ cd C2_Infrastructure
```


### Install all Necessary packages

```console
rfs@debian:~$ sudo ./install.sh
```


## Install Locally



```console
rfs@debian:~$ redlabs --install
```

```console
rfs@debian:~$ redlabs --config web --local
```




## Cloud Install
```console
rfs@debian:~$ redlabs --config web --aws
```
