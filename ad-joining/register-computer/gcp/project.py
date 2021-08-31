import googleapiclient.discovery

class Project(object):
    def __init__(self, project_id):
        self.__project_id = project_id
        self.__gce_client = googleapiclient.discovery.build('compute', 'v1')

    def get_zones(self):
        page_token = None
        zones = []

        while True:
            result = self.__gce_client.zones().list(
                project=self.__project_id,
                pageToken=page_token).execute()
            zones += [item["name"] for item in result["items"]]

            if not page_token:
                break

        return zones

    def get_instance_names(self, zones):
        page_token = None
        names = []

        for zone in zones:
            while True:
                result = self.__gce_client.instances().list(
                    project=self.__project_id,
                    zone=zone,
                    pageToken=page_token).execute()
                if "items" in result:
                    names += [item["name"] for item in result["items"]]

                if not page_token:
                    break

        return names
