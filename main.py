import threading
import subprocess
import importlib
from paddle import PaddleThread
def exec_paddle(script):
    subprocess.run(['python', script])

def exec_state(script, pThread):
    module = importlib.import_module(script[:-3])
    module.main(pThread)

def main():
    state = 'state.py'
    paddle = 'paddle.py'

    thread_pc = PaddleThread("paddle", 1000)
    thread_state = threading.Thread(target = exec_state, args = (state,thread_pc))
    

    thread_state.start()
    thread_pc.start()

    thread_state.join()
    thread_pc.join()

if __name__ == '__main__':
    main()