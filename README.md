hands detection movement:

introduction:


steps 1:
Guide line:

-install python 3.11 jangan version 3.13 sebab mediapipe tak support lagi version tu

-bukan command prompt
```bash
python --version
```
-tengok betul ke tak version yang anda telah install
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Perhatian !!

jika di dalam laptop anda sudah mempunyai python tetapi python anda yang latest contohnya macam saya , saya sudah ada python 3.13.3 version
jadi Langkah nya akan jadi lain.

-Perhatian (**Langkah ini hanya untuk orang yang mempunyai python version yang lebih dari 3.11**)

-anda boleh create env tanpa anda perlu install python baru 

-- buat virtual environment:
```bash
py -3.11 -m venv myenv
```
"myenv" tu anda boleh tukar mengikut pada diri anda kerana itu adalah nama env anda

-python3.11 → gunakan Python versi 3.11
-m venv → module untuk buat virtual environment
-myenv → nama folder environment

Folder myenv akan muncul dalam directory .
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
activate virtual environment

Windows (cmd):
```bash
myenv\Scripts\activate
```

Windows(Powershell):
```bash
.\myenv\Scripts\Activate.ps1
```

Mac/Linux:
```bash

source myenv/bin/activate
```



