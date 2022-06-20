from . import main

@main.route('/')
def main():
    return "<p> Hello to my amazing Flask App </p>"