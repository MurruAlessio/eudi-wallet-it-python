# eudi-wallet-it-python

![CI build](https://github.com/italia/eudi-wallet-it-python/workflows/eudi_wallet_python/badge.svg)
![Python version](https://img.shields.io/badge/license-Apache%202-blue.svg)
![py-versions](https://img.shields.io/badge/python-3.10-blue.svg)
[![GitHub issues](https://img.shields.io/github/issues/italia/eudi-wallet-it-python.svg)](https://github.com/italia/eudi-wallet-it-python/issues)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)
[![Join the #spid openid](https://img.shields.io/badge/Slack%20channel-%23spid%20openid-blue.svg)](https://developersitalia.slack.com/archives/C7E85ED1N/)

EUDI Wallet Python toolchain is a suite of Python libraries designed to
make it easy the implementation of an EUDI Wallet Relying Party according 
to the [Italian specification](https://italia.github.io/eudi-wallet-it-docs/en/).

> Please note: the scope of this project is giving tools and helpers to build a EUDI Wallet compliant to the national specs. All the components listed below are tailored to this scope.

The toolchain contains the following components:

| Name | Description |
| :--- | --- |
| __tools.jwk__ | Creation of JSON Web Key (JWK) according to [RFC7517](https://datatracker.ietf.org/doc/html/rfc7517). | refs to docs |
| __tools.jwt__ | Creation of signed or encrypted JSON Web Token (JWT) according to [RFC7519](https://datatracker.ietf.org/doc/html/rfc7519), [RFC7515](https://datatracker.ietf.org/doc/html/rfc7515) and [RFC7516](https://datatracker.ietf.org/doc/html/rfc7516) | refs to docs |
| __tools.ui.qrcode__ | Creation of QRCodes | refs to docs |
| __oauth2.dpop__ | Tools for issuing and parsing DPoP artifacts, according to [OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-dpop) | refs to docs |
| __oauth2.par__ | Tools for issuing and parsing Pushed Authorization Requests, according to [OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) | refs to docs |
| __openid4vp.request__ | Tools for issuing [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) requests objects | refs to docs |
| __openid4vp.redirect__ | Tools for parsing [OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) responses | refs to docs |
| __openid4vp.federation__ | OpenID Connect Federation Wallet Relying Party Entities and Trust Mechanisms | refs to docs |
| __dif.presentation_exchange__ | [DiF Presentation Exchange 2.0](https://identity.foundation/presentation-exchange/) | refs to docs |
| __satosa.openid4vp.backend__ | SATOSA Openid4VP Relying Party backend | refs to docs |


## Setup

Install enviroment and dependencies
````
apt install python3-dev python3-pip git
python3 -m pip install --upgrade pip
sudo pip install virtualenv
````

Activate the environment. It's optional and up to you if you want to install 
in a separate env or system wide
````
virtualenv -p python3 env
source env/bin/activate
````

Install using pip

`pip install eudi-wallet-python`

Install using github

`pip install git+https://github.com/italia/eudi-wallet-it-python`


## Example project

The example project is a docker-compose that runs a demo composed by the following component:

- Wordpress with SAML2 support and Bootstrap Italia template preregistered to the IAM Proxy.
- Satosa-Saml2Spid IAM Proxy with a preconfigured OpenID4VP backend

## Satosa configuration

See [README-SATOSA.md](README-SATOSA.md).

## Contribute

Your contribution is welcome, no question is useless and no answer is obvious, we need you.

#### Contribute as end user

Please open an issue if you've found a bug or if you want to ask some features.

#### Contribute as developer

Please open your Pull Requests on the __dev__ branch. 
Please consider the following branches:

 - __main__: where we merge the code before tag a new stable release.
 - __dev__: where we push our code during development.
 - __other-custom-name__: where a new feature/contribution/bugfix will be handled, revisioned and then merged to dev branch.

## Authors

- Giuseppe De Marco
- Pasquale De Rose
- Alessio Amurri
- Nicola ...
- ...
