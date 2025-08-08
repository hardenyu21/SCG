from e2b_code_interpreter import Sandbox, TimeoutException

import os
os.environ["E2B_API_KEY"] = "e2b_abb5349a7b64ec837ae4dce1b7830e37ee5baa0e"

if __name__ == "__main__":
    with open("response274_7b.txt", "r") as f:
        code = f.read()
    try:
        with Sandbox() as sandbox:
            execution = sandbox.run_code(code, timeout=10)
            result = execution.text
        
        # The original logic: check if the output is the string 'True'
            print(result == 'True')

    except TimeoutException:
        # If sandbox.run_code exceeds its time limit, this block will be executed.
        # As requested, treat the timeout as a failure (False).
        print("Timeout")
        
    except Exception as e:
        print(e)