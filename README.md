# matomai_task

octree visualization using open3d library

## Installation process

My enviroment: Windows 10 64-bit, python 3.10.11

Install process:
```bash
python3 -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

If errors: please refer to open3d docs for installation in-depth guide [Getting started with open3d](http://www.open3d.org/docs/release/getting_started.html)

## Launching

Before launching, las file provided must be inserted into project root (./), and renamed `las_data.las`,
or FILE_PATH parameter must be set in `main.py`.

Main program is in `main.py`, so this file must be executed with python3

```bash
python3 main.py
```



