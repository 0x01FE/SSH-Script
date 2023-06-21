import os
from argparse import ArgumentParser


private_key = ''
public_key = ''



def copy(usb_path : str, home_path : str) -> None:

    if not os.path.exists(usb_path):
        print('Given USB path does not exist!')
        exit()

    if not os.path.exists(f'{home_path}/.ssh'):
        os.mkdir(f'{home_path}/.ssh')

    print('Reading public key from USB...')
    with open(f'{usb_path}{public_key}', 'rb') as f:
        public_key_data = f.read()

    print('Writing to user\'s .shh directory...')
    with open(f'{home_path}/.ssh/{public_key}', 'wb') as f:
        f.write(public_key_data)

    print('Reading private key from USB...')
    with open(f'{usb_path}{private_key}', 'rb') as f:
        private_key_data = f.read()

    print('Writing to user\'s .ssh directory...')
    with open(f'{home_path}/.ssh/{private_key}', 'wb') as f:
        f.write(private_key_data)

    print('Transfer Complete!')



def remove(home_path : str) -> None:

    print('Removing public key from device...')
    os.remove(f'{home_path}/.ssh/{public_key}')

    print('Removing private key from device...')
    os.remove(f'{home_path}/.ssh/{private_key}')

    print('Keys removed!')



def main() -> None:
    parser = ArgumentParser()

    parser.add_argument("-r", "--remove", help="Tell the script to remove the keys from your machine.", action='store_true', required=False)
    parser.add_argument("-p", "--path", help="Path the USB (Default on POSIX system is /mnt/usb, Windows is D:).", required=False)

    args = parser.parse_args()

    if os.name == 'posix':
        home_path = os.getenv('HOME')

        if not args.path:
           args.path = '/mnt/usb/'

        if args.remove:
            remove(home_path)

        else:
            copy(args.path, home_path)

    elif os.name == 'nt':
        home_path = f'{os.getenv("HOMEDRIVE")}{os.getenv("HOMEPATH")}'

        if not args.path:
            args.path = 'D:/'

        if args.remove:
            remove(home_path)

        else:
            copy(args.path, home_path)

    else:
        print("I have no idea what OS you're using my bad.")



if __name__ == "__main__":
    main()
