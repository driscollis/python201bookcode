from .module_y import spam as ham

def main():
    ham()

if __name__ == '__main__':
    # This won't work!
    main()