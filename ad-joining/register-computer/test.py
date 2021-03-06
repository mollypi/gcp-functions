import requests
import google.auth
import google.auth.transport.requests

OAUTH_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'

def __get_id_token(target_audience):
    bootstrap_credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/iam'])
    bootstrap_credentials.refresh(google.auth.transport.requests.Request())

    # Construct OAuth 2.0 service account credentials using the signer
    # and email acquired from the bootstrap credentials.
    # By using the 'target_audience' claim, we cause an IdToken to
    # be created.
    service_account_credentials = google.oauth2.service_account.Credentials(
        bootstrap_credentials.signer,
        bootstrap_credentials.service_account_email,
        token_uri=OAUTH_TOKEN_URI,
        additional_claims={
            "target_audience": target_audience,
        })

    # service_account_credentials gives us a JWT signed by the service
    # account. Next, we use that to obtain an OpenID Connect token,
    # which is a JWT signed by Google.
    token_response = google.oauth2._client._token_endpoint_request(
        google.auth.transport.requests.Request(),
        OAUTH_TOKEN_URI,
        {
        'assertion':  service_account_credentials._make_authorization_grant_assertion(),
        'grant_type': google.oauth2._client._JWT_GRANT_TYPE,
    })

    return token_response["id_token"]

if __name__ == "__main__":
    headers = {
        "Authorization": "Bearer " + __get_id_token("https://localhost:5000/")
    }

    response = requests.post("http://localhost:5000/cleanup", headers=headers)
    print(response.text)
