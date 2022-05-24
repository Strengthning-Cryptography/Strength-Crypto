python -m venv venv

source ./venv/bin/activate

pip list && which pip && which python

pip install qiskit

pip install matplotlib pylatexenc

pip install pycryptodome

pip list

(command -v apt-get > /dev/null && sudo apt-get install python-tk)   || \
(command -v pacman > /dev/null && sudo pacman -S tk)                 || \
(command -v dnf > /dev/null && sudo dnf install python3-tkinter)     || \
(command -v yum > /dev/null && sudo yum install -y tkinter tk-devel) || \
echo "Installing TKinter failed"
