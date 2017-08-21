from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from PIL import Image
import os

input = getattr(__builtins__, 'raw_input', input)

def main():
    redirect_uri = "http://localhost:8080/"
    client_secret = "BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM"

    client = onedrivesdk.get_default_client(client_id='00000000481695BB',
                                            scopes=['wl.signin',
                                                    'wl.offline_access',
                                                    'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    # Finally, authenticate!
    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    # Define variables
    item_id = "root"
    copy_item_ids = None
    action = 0

    # Accept user input
    action = int(input("Input 1 to Upload..."))
    # Once user approves upload by pressing 1 - proceeed with upload of newfile.txt

    if action == 1:
        # Let the user know that the upload has started.
        print("Uploading...")
        # This actually uploads the file, taken from the github documents.
        returned_item = client.item(drive='me', id='root').children['newfile.txt'].upload('./newfile.txt')

    else:
        item_id = items[selected-1].id

def upload(client, item_id):
    client.item(id=item_id).children[name].upload(directory)


def get_parent_id(client, item_id):
    id = client.item(id=item_id).get().parent_reference.id
    return id

if __name__ == "__main__":
    main()
