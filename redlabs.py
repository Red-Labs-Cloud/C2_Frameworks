import argparse


def install_local(config_file):
  print(f"Installing software based on config: {config_file}")

def configure(config_file):
  print(f"Configuring software based on config: {config_file}")

def delete():
  print("Deleting software and configuration")

def main():
  parser = argparse.ArgumentParser(
                    prog='Red Labs',
                    description='Red Labs Cloud installer',
                    epilog='Martian Defense Team')
  parser.add_argument("action", choices=["install", "delete"], help="What we can do - for now...")
  parser.add_argument("local", choices=["local", "Any Linux", "ProxMox","VmWare"], help="Deploy to Anywhere")
  parser.add_argument("cloud", choices=["digitalOcean", "AWS", "Azure","GCP"], help="Deploy to any Cloud")
  parser.add_argument("-i", "--install", required=True, help="Install the Labs")
  parser.add_argument("-c", "--config", dest="config_file", required=False, help="Configure the Labs")
  parser.add_argument("-d", "--delete", required=False, help="Delete the Labs")
  args = parser.parse_args()

  if args.action == "install" and args.local == 'local':
    install_local(args.config_file)
  elif args.action == "config":
    configure(args.config_file)
  elif args.action == "delete":
    delete()
  else:
    print(f"Invalid action: {args.action}")

if __name__ == "__main__":
  main()