from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1662071653:AAGOBPWghWUP4Z5eh5pQ7zKcTZWyROPAhgE"
    APP_ID = 3488239
    API_HASH = "21f90bb0ad5ca8bf276daeb043070bd7"
    OWNER_ID = 1304407489
    AUTH_CHANNEL = [-1001424948459]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[TorrentGenerator_Bot]
type = drive
scope = drive
root_folder_id = 1Ss-FUl2rRaTiLk1lq74yAcmj5i8dPJXj
token = {"access_token":"ya29.A0AfH6SMCnpzkVSL96IiMcNKef1Q0tAgqaJ9UqIIf-vBqzNQ2911iGQE5pJAjIapCipbtlC441sHStj84tXXPRxwE_qxb7E2E3xwq79wobky6Ow6flhk366Ld1LXncVodgJDke0lUV8c5saRLBimrn0pgsmHvb","token_type":"Bearer","refresh_token":"1//0g4JPYyDMkDucCgYIARAAGBASNwF-L9IrebVKrFnIdxrCVqK1Id-Ot6qdZPPSg-Bkn3iqIg07KkpPcE2ESiuS25Ymk7p4gGsJccY","expiry":"2021-02-24T19:54:46.0239209+05:30"}
team_drive = 0AKM0e85jWxEpUk9PVA
"""
