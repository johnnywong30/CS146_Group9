# CS146_Group9
Final Project Repository For CS146 Group 9

## How To Run - Assuming Python3 is installed...
### Create a Virtual Environment
A virtual environment is important in order to create an isolated Python environment to run code with specific dependencies exclusive to the virtual environment.
1. In a terminal, navigate to your home directory (eg. `cd ~`). You should be already there in a new terminal instance.
2. Run `python3 -m venv <venv_name>` (replace `venv_name` with whatever name you'd like)
3. Activate the virtual environment by running `source <venv_name>/bin/activate`
4. The computer's name should be preceded by `(venv_name)` now. You are inside your virtual environment.
5. You can deactivate the virtual environment by running the command `deactivate`
6. The virtual environment can be activated from any current working directory (as long as it was saved in the home directory with the command `source ~/<venv_name>/bin/activate`

### Install Our Dependencies
After activating the virtual environment, our dependencies need to be installed in order for our Flask app to run.
1. Make sure your current working directory is `<path-to-this-project>/CS146_Group9`
2. Install our dependencies with `pip install -r requirements.txt`

### Run our Flask App
1. Run `python app.py` (Has to be python3)
2. Open `localhost:5000` in a browser
