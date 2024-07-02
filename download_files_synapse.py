import synapseclient
import synapseutils
import argparse

def sync_files_from_synapse(auth_token, syn_id, local_path):
	# Initialize a Synapse client
	syn = synapseclient.Synapse()

	# Log in to Synapse using an authentication token
	syn.login(authToken=auth_token)

	# Sync files from Synapse to a local directory
	files = synapseutils.syncFromSynapse(syn, syn_id, path=local_path)
	return files

def main():
	# Set up argument parsing
	parser = argparse.ArgumentParser(description='Sync files from Synapse.')
	parser.add_argument('auth_token', type=str, help='Your Synapse authentication token')
	parser.add_argument('syn_id', type=str, help='The Synapse ID of the project or folder to sync')
	parser.add_argument('local_path', type=str, help='The local directory to sync files to')

	# Parse arguments
	args = parser.parse_args()

	# Call the sync function with the parsed arguments
	sync_files_from_synapse(args.auth_token, args.syn_id, args.local_path)

if __name__ == '__main__':
	main()
