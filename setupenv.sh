export FLASK_APP=siem.py
export LANG=C.UTF-8
export LC_ALL=C.UTF-8

ureq() {
    # update requiremests if new package is instaled
    pip freeze > requirements.txt
}

run() {
    flask run --host 0.0.0.0
}
