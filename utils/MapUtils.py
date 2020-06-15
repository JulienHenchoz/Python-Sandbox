class MapUtils:

    @staticmethod
    def point_to_pos(pos, tile_size, camera_offset):
        pos_x, pos_y = pos
        tile_width, tile_height = tile_size
        camera_offset_x, camera_offset_y = camera_offset
        tile_width_half = tile_width / 2
        tile_height_half = tile_height / 2
        pos_x = pos_x - camera_offset_x - tile_width_half
        pos_y = pos_y - camera_offset_y


        return (
                int((pos_x / tile_width_half + pos_y / tile_height_half) / 2),
                int((pos_y / tile_height_half - pos_x / tile_width_half) / 2)
        )

    @staticmethod
    def pos_to_point(pos, tile_size, camera_offset):
        x, y = pos
        tile_width, tile_height = tile_size
        camera_offset_x, camera_offset_y = camera_offset
        tile_width_half = tile_width / 2
        tile_height_half = tile_height / 2

        return (
                (x * tile_width_half) - (y * tile_width_half) + camera_offset_x,
                (x * tile_height_half) + (y * tile_height_half) + camera_offset_y
        )