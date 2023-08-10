import datetime

from cryptojwt.jws.jws import JWS
from cryptojwt.jwk.rsa import new_rsa_key

import pyeudiw.federation.trust_chain_validator as tcv_test


def iat_now() -> int:
    return int(datetime.datetime.now(datetime.timezone.utc).timestamp())

def exp_from_now(minutes: int = 33) -> int:
    now = datetime.datetime.now(datetime.timezone.utc)
    return int((now + datetime.timedelta(minutes=minutes)).timestamp())

NOW = iat_now()
EXP = exp_from_now(50)

# Define intermediate ec
intermediate_jwk = new_rsa_key()

# Define TA ec
ta_jwk = new_rsa_key()

# Define leaf Credential Issuer
leaf_cred_jwk = new_rsa_key()
leaf_cred = {
    "exp": EXP,
    "iat": NOW,
    "iss": "https://credential_issuer.example.org",
    "sub": "https://credential_issuer.example.org",
    'jwks': {"keys": []},
    "metadata": {
        "openid_credential_issuer": {
            'jwks': {"keys": []}
        },
        "federation_entity": {
            "organization_name": "OpenID Wallet Verifier example",
            "homepage_uri": "https://verifier.example.org/home",
            "policy_uri": "https://verifier.example.org/policy",
            "logo_uri": "https://verifier.example.org/static/logo.svg",
            "contacts": [
                "tech@verifier.example.org"
            ]
        }
    },
    "authority_hints": [
        "https://intermediate.eidas.example.org"
    ]
}

leaf_cred['jwks']['keys'] = [leaf_cred_jwk.serialize()]
leaf_cred['metadata']['openid_credential_issuer']['jwks']['keys'] = [leaf_cred_jwk.serialize()]


# Define intermediate Entity Statement for credential
intermediate_es_cred = {
    "exp": EXP,
    "iat": NOW,
    "iss": "https://intermediate.eidas.example.org",
    "sub": "https://credential_issuer.example.org",
    'jwks': {"keys": []}
}

intermediate_es_cred["jwks"]['keys'] = [leaf_cred_jwk.serialize()]

# Define leaf Wallet Provider
leaf_wallet_jwk = new_rsa_key()
leaf_wallet = {
    "exp": EXP,
    "iat": NOW,
    "iss": "https://wallet-provider.example.org",
    "sub": "https://wallet-provider.example.org",
    'jwks': {"keys": []},
    "metadata": {
        "wallet_provider": {
            "jwks":  {"keys": []}
        },
        "federation_entity": {
            "organization_name": "OpenID Wallet Verifier example",
            "homepage_uri": "https://verifier.example.org/home",
            "policy_uri": "https://verifier.example.org/policy",
            "logo_uri": "https://verifier.example.org/static/logo.svg",
            "contacts": [
                "tech@verifier.example.org"
            ]
        }
    },
    "authority_hints": [
        "https://intermediate.eidas.example.org"
    ]
}

leaf_wallet['jwks']['keys'] = [leaf_wallet_jwk.serialize()]
leaf_wallet['metadata']['wallet_provider'] = [leaf_wallet_jwk.serialize()]

# Define intermediate Entity Statement for wallet provider
intermediate_es_wallet = {
    "exp": EXP,
    "iat": NOW,
    "iss": "https://intermediate.eidas.example.org",
    "sub": "https://wallet-provider.example.org",
    'jwks': {"keys": []}
}

intermediate_es_wallet["jwks"]['keys'] = [leaf_wallet_jwk.serialize()]

# Define TA
ta_es = {
    "exp": EXP,
    "iat": NOW,
    "iss": "https://trust-anchor.example.eu",
    "sub": "https://intermediate.eidas.example.org",
    'jwks': {"keys": []},
    "trust_marks": [
        {
            "id": "https://trust-anchor.example.eu/federation_entity/that-profile",
            "trust_mark": "eyJhb …"
        }
    ]
}

ta_es["jwks"]['keys'] = [intermediate_jwk.serialize()]

# Sign step

leaf_cred_signer = JWS(leaf_cred, alg='RS256', typ='application/entity-statement+jwt')
leaf_cred_signed = leaf_cred_signer.sign_compact([leaf_cred_jwk])

leaf_wallet_signer = JWS(leaf_wallet, alg='RS256', typ='application/entity-statement+jwt')
leaf_wallet_signed = leaf_wallet_signer.sign_compact([leaf_wallet_jwk])


intermediate_signer_es_cred = JWS(intermediate_es_cred, alg='RS256', typ='application/entity-statement+jwt')
intermediate_es_cred_signed = intermediate_signer_es_cred.sign_compact([intermediate_jwk])

intermediate_signer_es_wallet = JWS(intermediate_es_wallet, alg='RS256', typ='application/entity-statement+jwt')
intermediate_es_wallet_signed = intermediate_signer_es_wallet.sign_compact([intermediate_jwk])

ta_signer = JWS(ta_es, alg="RS256", typ="application/entity-statement+jwt")
ta_es_signed = ta_signer.sign_compact([ta_jwk])

trust_chain_cred = [
    leaf_cred_signed,
    intermediate_es_cred_signed,
    ta_es_signed
]

trust_chain_wallet = [
    leaf_wallet_signed,
    intermediate_es_wallet_signed,
    ta_es_signed
]

test_cred = tcv_test.StaticTrustChainValidator(trust_chain_cred, [ta_jwk.serialize()])
test_wallet = tcv_test.StaticTrustChainValidator(trust_chain_wallet, [ta_jwk.serialize()])
# breakpoint()

print (ta_jwk.serialize())

# print(test_cred.is_valid)
# print(test_wallet.is_valid)
# print(trust_chain_cred)

