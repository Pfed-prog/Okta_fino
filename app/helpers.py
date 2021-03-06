import asyncio
from okta_jwt_verifier import JWTVerifier


loop = asyncio.get_event_loop()

def is_access_token_valid(token, issuer, client_id):
    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_access_token(token))
        return True
    except Exception:
        return False


def is_id_token_valid(token, issuer, client_id, nonce):
    jwt_verifier = JWTVerifier(issuer, client_id, 'api://default')
    try:
        loop.run_until_complete(jwt_verifier.verify_id_token(token, nonce=nonce))
        return True
    except Exception:
        return False

config = {
  "auth_uri": "",
  "client_id": "",
  "client_secret": "",
 "redirect_uri": "http://localhost:8080/authorization-code/callback",
  "issuer": "",
  "token_uri": "",
  "userinfo_uri": ""
}