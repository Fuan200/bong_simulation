import threading
import subprocess
import importlib

def exec_paddle(script):
    subprocess.run(['python', script])

def exec_state(script):
    module = importlib.import_module(script[:-3])
    module.main()

def main():
    state = 'state.py'
    paddle = 'paddle.py'

    thread_state = threading.Thread(target = exec_state, args = (state,))
    thread_pc = threading.Thread(target = exec_paddle, args = (paddle,))

    thread_state.start()
    thread_pc.start()

    thread_state.join()
    thread_pc.join()

if __name__ == '__main__':
    main()