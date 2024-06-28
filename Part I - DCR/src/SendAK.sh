#!/bin/sh

# Variables
KEY_VAULT_NAME="gesKeyVault"
SECRET_NAME="gesSecret"
AK_PUBLIC_KEY_FILE="/home/azureuser/rsa_ak.pub"
RESOURCE_GROUP="mercurycodes-ges24_group"

# Read AK public key
echo "Reading AK public key from file: $AK_PUBLIC_KEY_FILE"
AK_PUBLIC_KEY=$(cat $AK_PUBLIC_KEY_FILE)

if [ $? -ne 0 ]; then
    echo "Failed to read the AK public key file"
    exit 1
fi

# Display the public key content for debugging
echo "AK Public Key Content: $AK_PUBLIC_KEY"

# Encoding in Base64
AK_PUBLIC_KEY_BASEE64=$(echo -n "$AK_PUBLIC_KEY" | base64)

# Display base64 encoding
echo "Base64 Encoded AK Key: $AK_PUBLIC_KEY_BASE64"

# Save AK key as a secret in Key Vault Server
az keyvault secret set --vault-name $KEY_VAULT_NAME --name $SECRET_NAME --value "$AK_PUBLIC_KEY_BASE64"