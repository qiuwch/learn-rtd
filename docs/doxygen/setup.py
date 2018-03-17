from distutils.core import setup
import sys, os

with open('test.txt', 'w') as f:
    f.write('This is a test message')

with open('/home/qiuwch/workspace/learn-rtd/docs/test.txt', 'w') as f:
    f.write('This is a test message\n')
    # f.write(os.path.curdir)
    # f.write(os.path.abspath('.'))
    f.write(__file__)

print 'Install this file'
print 'Hello world.'
print os.path.curdir
sys.stdout.write('Test')
sys.stderr.write('Test')
setup(name='build-doxygen',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=[],
     )
