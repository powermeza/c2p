from cx_Freeze import setup, Executable

setup(name='c2p',
      version='1.0',
      description='CSV converter to Pipe separeted file',
      executables=[Executable("c2pv3.py")])
