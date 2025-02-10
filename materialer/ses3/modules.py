import os
import subprocess

# os.chdir('materialer/ses3')
# os.mkdir('test')
# os.chdir('test')

# with open('claus.py', 'w') as f:
#     f.write('import os')

os.makedirs('clbo', exist_ok=True)


print(    subprocess.run(['git', 'clone', 'https://github.com/python-elective-kea/IntroPythonSpring2025.git'])    )
