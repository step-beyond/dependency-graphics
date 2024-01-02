from dataclasses import dataclass


@dataclass
class DrawConfig:
    draw_config: any

    def is_show_graph(self) -> bool:
        return self.draw_config.get("show-graph")

    def get_color_matching(self) -> []:
        if self.draw_config.get("color-matching") is None:
            return []
        return self.draw_config.get("color-matching")

    def get_filename(self) -> []:
        return self.draw_config.get("filename")
