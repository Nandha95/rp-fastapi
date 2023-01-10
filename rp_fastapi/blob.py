import os
from typing import Container
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError

class BlobClient:
    """
    BlobClient

    Example:
        ## Init client object
        from catmanbase.storage_service import BlobStorageWrapper

        client = BlobStorageWrapper(connection_string, container)

        ## Download a blob
        client.download(<blob-path>)

        ## Upload
        client.upload(<bytes-to-upload>, <blob-path>)
    """

    def __init__(self, connect_str, container) -> None:
        try:
            if not connect_str:
                print("AZURE_STORAGE_CONNECTION_STRING required.")
                raise KeyError

            # Instantiate a blob service client using a connection string
            service_client = BlobServiceClient.from_connection_string(connect_str)

            # # Create and Instantiate a blob container client from service client
            # try:
            #     _ = service_client.create_container(container)
            # except ResourceExistsError:
            #     print("Container already exists. Instantiating client.")
            self.client = service_client.get_container_client(container)
        except Exception as ex:
            print("Exception: ", ex)
            raise ex

    def download(self, blob, download_dir=None, return_type="bytesIO"):
        """
        Download a file and returns as bytesIO/bytes or writes to download dir if not None.

        Args:
            blob: str
            download_dir: str, default=None
            return_type: str, [bytesIO, bytes], default='BytesIO' \
                no impact if download_dir is set
        Returns:
            BytesIO | Bytes | str
        """
        from io import BytesIO
        my_blobs = self.client.list_blobs()
        print(my_blobs)
        try:
            data = self.client.download_blob(blob=blob)
            if download_dir:
                os.makedirs(download_dir, exist_ok=True)
                download_file = os.path.join(download_dir, os.path.basename(blob))
                with open(download_file, "wb") as file:
                    file.write(data.readall())
                    return download_file

            if return_type == "bytesIO":
                return BytesIO(data.readall())
            elif return_type == "bytes":
                return data.readall()
            else:
                print("Invalid return type. Possible value is bytesIO or bytes")
                return None
        except ResourceNotFoundError:
            print(f"Blob: {blob} does not exist")
            return None
        except Exception as ex:
            print("Download Failed!!! Exception: ", ex)
            raise ex

    def upload(self, data, blob):
        """
        Upload the data to target blob in blob storage

        Args:
            data: bytes
                data that needs to be uploaded
            blob: str
                blob path in blob storage

        Returns:
            None
        """
        try:
            self.client.upload_blob(name=blob, data=data, overwrite=True)
        except ResourceExistsError as ex:
            print("Blob already exists. Cannot re-upload on same blob.")
        except Exception as ex:
            print("Upload Failed!!! Rolling back any changes")
            self.delete(blob)
            print("Upload Exception: ", ex)
            raise ex

    def delete(self, blob):
        """
        Deletes blob from blob storage

        Args:
            blob: str
                Blob that you wants to delete from azure blob storage
        Returns:
            None
        """
        try:
            self.client.delete_blob(blob)
        except ResourceNotFoundError:
            print(f"Blob {blob} does not exist. Nothing to delete!!!")
        except Exception as ex:
            print("Exception:", ex)
            raise ex
    def download(self, blob, download_dir=None, return_type="bytesIO"):
        """
        Download a file and returns as bytesIO/bytes or writes to download dir if not None.

        Args:
            blob: str
            download_dir: str, default=None
            return_type: str, [bytesIO, bytes], default='BytesIO' \
                no impact if download_dir is set
        Returns:
            BytesIO | Bytes | str
        """
        from io import BytesIO
        my_blobs = self.client.list_blobs()
        try:
            data = self.client.download_blob(blob=blob)
            if download_dir:
                os.makedirs(download_dir, exist_ok=True)
                download_file = os.path.join(download_dir, os.path.basename(blob))
                with open(download_file, "wb") as file:
                    file.write(data.readall())
                    return download_file

            if return_type == "bytesIO":
                return BytesIO(data.readall())
            elif return_type == "bytes":
                return data.readall()
            else:
                print("Invalid return type. Possible value is bytesIO or bytes")
                return None
        except ResourceNotFoundError:
            print(f"Blob: {blob} does not exist")
            return None
        except Exception as ex:
            print("Download Failed!!! Exception: ", ex)
            raise ex

    def upload_file(self, file_path, blob):
        """
        Uploads file to blob storage

        Args:
            file_path: str
                File path to local file that needs to uploaded to blob storage
            blob: str
                The blob path in azure blob storage
        Returns:
            None
        """
        try:
            with open(file_path, "rb") as data:
                self.upload(data, blob)
        except Exception as ex:
            print("Upload Failed!!! Rolling back any changes")
            self.delete(blob)
            print("Upload Exception: ", ex)
            raise ex

    def upload_stream(self, data_stream, blob):
        """
        WIP
        """
        # TODO - WIP
        try:
            pass
        except Exception as ex:
            pass


if __name__ == '__main__':
    pass