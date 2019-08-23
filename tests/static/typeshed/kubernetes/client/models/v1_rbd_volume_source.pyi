# Stubs for kubernetes.client.models.v1_rbd_volume_source (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1RBDVolumeSource:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    fs_type: Any = ...
    image: Any = ...
    keyring: Any = ...
    monitors: Any = ...
    pool: Any = ...
    read_only: Any = ...
    secret_ref: Any = ...
    user: Any = ...
    def __init__(self, fs_type: Optional[Any] = ..., image: Optional[Any] = ..., keyring: Optional[Any] = ..., monitors: Optional[Any] = ..., pool: Optional[Any] = ..., read_only: Optional[Any] = ..., secret_ref: Optional[Any] = ..., user: Optional[Any] = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def image(self): ...
    @image.setter
    def image(self, image: Any) -> None: ...
    @property
    def keyring(self): ...
    @keyring.setter
    def keyring(self, keyring: Any) -> None: ...
    @property
    def monitors(self): ...
    @monitors.setter
    def monitors(self, monitors: Any) -> None: ...
    @property
    def pool(self): ...
    @pool.setter
    def pool(self, pool: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...