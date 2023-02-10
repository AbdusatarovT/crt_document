from core.app import create_app

context = create_app()

if __name__ == '__main__':
    context.run(debug=True)