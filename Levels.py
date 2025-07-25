from DataValues import Constants, Assets
from DataValues.TypeAliases import Tcolor, dictStrAny, Tvec2
from Platform import Platform
from Interaction import Interaction
from pygame import Vector2, Color

class Level:
    def __init__(self, name: str, tags: list[str], platforms: list[Platform], interactions: dict[str, list[Interaction]], checkpoints: list[Tvec2], size: Vector2 = Vector2(Constants.SCREEN_SIZE), background: Color = Assets.BLACK):
        self.name = name
        self.tags = tags
        self.size: Vector2 = size
        self.platforms = platforms
        self.top_collision_interactions = interactions.get("top_collision", [])
        self.bottom_collision_interactions = interactions.get("bottom_collision", [])
        self.side_collision_interactions = interactions.get("side_collision", [])
        self.frame_interactions = interactions.get("frame", [])
        self.checkpoints = checkpoints
        self.background = background
        self.data: dictStrAny = {}

    def to_dict(self) -> dictStrAny:
        return {
            "name": self.name,
            "tags": self.tags,
            "size": [self.size.x, self.size.y],
            "platforms": [platform.to_dict() for platform in self.platforms],
            "interactions": {
                "top_collision": [inter.to_dict() for inter in self.top_collision_interactions],
                "bottom_collision": [inter.to_dict() for inter in self.bottom_collision_interactions],
                "side_collision": [inter.to_dict() for inter in self.side_collision_interactions],
                "frame": [inter.to_dict() for inter in self.frame_interactions]
            },
            "checkpoints": self.checkpoints,
            "background": [self.background.r, self.background.g, self.background.b]
        }

    def Grow(self, amount: int, direction: str):
        match direction:
            case "Up":
                self.size.y += amount

                for platform in self.platforms:
                    platform.rect.y += amount
            case "Down":
                self.size.y += amount
            case "Left":
                self.size.x += amount

                for platform in self.platforms:
                    platform.rect.x += amount
            case "Right":
                self.size.x += amount

    def Shrink(self, amount: int, direction: str):
        match direction:
            case "Up":
                self.size.y -= amount

                for platform in self.platforms:
                    platform.rect.y -= amount
            case "Down":
                self.size.y -= amount
            case "Left":
                self.size.x -= amount

                for platform in self.platforms:
                    platform.rect.x -= amount
            case "Right":
                self.size.x -= amount

    @classmethod
    def from_dict(cls, data: dictStrAny) -> "Level":
        return cls(data["name"], data["tags"], [Platform.from_dict(platform) for platform in data["platforms"]], {
            inter_type: [Interaction.from_dict(inter) for inter in inters] for inter_type, inters in data.get("interactions", {"top_collision": [], "bottom_collision": [], "side_collision": [], "frame": []}).items()
        }, data["checkpoints"], Vector2(data["size"]), Color(data["background"]))

    @classmethod
    def new_level(cls, name: str) -> "Level":
        return cls(name, [], [], {}, [])