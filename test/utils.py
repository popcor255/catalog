import sys
import yaml

def add_sidecar_to_yaml_file():
    with sys.stdin as file:
        # Load yaml file passed by stdin
        data = yaml.load(file, Loader=yaml.FullLoader)
        # If sidecars doesnt have any entries create an array for data manipulation
        if 'sidecars' not in data['spec']:
            data['spec']['sidecars'] = []
        # Append the local image registry to the yaml file
        data['spec']['sidecars'].append({"image": "registry", "name": "registry"})
        # Dump the changes to the stdout
        print(yaml.dump(data, default_flow_style=False))

if __name__ == '__main__':
    globals()[sys.argv[1]]()