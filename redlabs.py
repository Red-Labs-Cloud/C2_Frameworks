import argparse

def install(config_file):
  print(f"Installing software based on config: {config_file}")

def configure(config_file):
  print(f"Configuring software based on config: {config_file}")

def delete():
  print("Deleting software and configuration")

def main():
  parser = argparse.ArgumentParser(description="Software installer and configurator")
  parser.add_argument("action", choices=["install", "config", "delete"], help="Action to perform (install, config, or delete)")
  parser.add_argument("-i", "--install", dest="config_file", required=True, help="Configure the Labs")
  args = parser.parse_args()

  if args.action == "install":
    install(args.config_file)
  elif args.action == "config":
    configure(args.config_file)
  elif args.action == "delete":
    delete()
  else:
    print(f"Invalid action: {args.action}")

if __name__ == "__main__":
  main()