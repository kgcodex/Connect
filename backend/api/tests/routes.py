from enum import Enum

BASE = "/api/v1"


class Routes(str, Enum):
    REGISTER = f"{BASE}/register/"
    LOGIN = f"{BASE}/login/"
    REFRESH = f"{BASE}/refresh/"
    PROFILE = f"{BASE}/profile/"
    POST = f"{BASE}/post/"
    COMMENT = f"{BASE}/comments/"
    ALL_POST = f"{BASE}/all_posts/"
    SEARCH = f"{BASE}/search/"
    FEED = f"{BASE}/feed/"
    FOLLOWING = f"{BASE}/following/"
    FOLLOWER = f"{BASE}/follower/"
