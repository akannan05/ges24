#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

# Configuration
KEY_VAULT_NAME="gesKeyVault"
SECRET_NAME="gesSecret"

# Azure CLI command to retrieve secret
SECRET_VALUE=$(az keyvault secret show --vault-name $KEY_VAULT_NAME --name $SECRET_NAME --query value -o tsv)

if [ -z "$SECRET_VALUE" ]; then
  echo "Failed to retrieve secret from Azure Key Vault."
  exit 1
fi

# Evaluate the PCR value
echo "Evaluating PCR values..."
tpm2_pcrread

# Set variable for CRITICAL DATA using the secret value
echo "Setting variable for CRITICAL DATA..."
export SHA256_DATA=$(echo "$SECRET_VALUE" | openssl dgst -sha256 -binary | xxd -p -c 32)
export SHA1_DATA=$(echo "$SECRET_VALUE" | openssl dgst -sha1 -binary | xxd -p -c 20)

# Check the hash value of CRITICAL DATA
echo "SHA1_DATA: $SHA1_DATA"
echo "SHA256_DATA: $SHA256_DATA"

# Extend the hash of CRITICAL DATA to PCR 23
echo "Extending hash of CRITICAL DATA to PCR 23..."
tpm2_pcrextend 23:sha1=$SHA1_DATA,sha256=$SHA256_DATA

# Set service provider nonce
export SERVICE_PROVIDER_NONCE="12345678"

# Create Quote from PCR23
echo "Creating quote from PCR23..."
tpm2_quote \
  --key-context rsa_ak.ctx \
  --pcr-list sha1:23,sha256:23 \
  --message pcr_quote.plain \
  --signature pcr_quote.signature \
  --qualification $SERVICE_PROVIDER_NONCE

echo "Quote creation complete. Files generated: pcr_quote.plain, pcr_quote.signature"