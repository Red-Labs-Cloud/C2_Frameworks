import argparse
import os

def c2_local(config_file):
  print(f"Installing software based on config: {config_file}")
  os.system("ansible-playbook C2s/CobaltStrike/cs-install.yml -i ./local_host")

def install_cloud(config_file):
  os.system("ansible-playbook C2s/CobaltStrike/cs-install.yml -i ./cloud_hosts")

def delete():
  print("RFS Delete software and configuration---")

def main():
  base = argparse.ArgumentParser(
                    prog='Red Labs',
                    description='Red Labs Cloud installer',
                    epilog='Martian Defense Team')
  base.add_argument("-i", "--install",  action='store_true',required=False, help="Configure the Labs")
  base.add_argument("-c", "--config", dest="config_file", required=False, help="Configure the Labs")
  base.add_argument("-d", "--delete", required=False, help="Delete the Labs")
  
  deploy = base.add_argument_group('Deploy')
  deploy.add_argument('-l',"--local",  action='store_true',help='Localhost')
  deploy.add_argument('-dg', help='Digital Ocean Cloud')
  deploy.add_argument('-aws', help='AWS Cloud')
  deploy.add_argument('-azr', help='Azure Cloud')

  service = base.add_argument_group('Services')
  service.add_argument('--rl', "--relay",help='Relay')
  service.add_argument('--c2', "--command-control",help='C2')


  args = base.parse_args()

  if args.install and args.local and args.relay:
    c2_local(args.config_file)
  elif args.install == "cloud" and args.lh == "deploys":
    install_cloud(args.config_file)
  elif args.install == "delete":
    delete()
  else:
    print(f"Invalid action: {args.install}")

if __name__ == "__main__":
  main()