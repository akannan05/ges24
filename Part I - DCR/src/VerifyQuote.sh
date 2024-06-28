#!/bin/bash

# Empty for now...
export SERVICE_PROVIDER_NONCE="12345678"

tpm2_checkquote \
--public rsa_ak.pub \
--message pcr_quote.plain \
--signature pcr_quote.signature \
--qualification $SERVICE_PROVIDER_NONCE \
--pcr pcr.bin
