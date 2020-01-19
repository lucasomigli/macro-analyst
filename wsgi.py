"""
==================================================================
Note: refer to changelog for some elaboration on proposed changes
==================================================================
"""

from macroanalyst import create_app

def main():
    app = create_app()
    app.run(host='127.0.0.1', debug=True)

if __name__ == "__main__":
    main()